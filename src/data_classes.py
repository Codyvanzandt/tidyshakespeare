from lxml import etree
from src.constants import NAMESPACES


class Play:
    def __init__(self, play_root_node):
        self.root_node = play_root_node
        self.title = self.get_title()
        self.acts = self.get_acts()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.title})"

    def get_title(self):
        title_node = self.root_node.xpath(".//tei:title", namespaces=NAMESPACES)[0]
        return title_node.text

    def get_acts(self):
        return [
            Act(act_node) for act_node in self.root_node.xpath(".//tei:div[@type = 'act']", namespaces=NAMESPACES)
        ]


class Act:
    def __init__(self, act_root_node):
        self.root_node = act_root_node
        self.number = self.get_number()
        self.scenes = self.get_scenes()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.number})"

    def get_number(self):
        return int(self.root_node.get("n"))

    def get_scenes(self):
        return [
            Scene(scene_root) for scene_root in self.root_node.xpath(".//tei:div[@type = 'scene']", namespaces=NAMESPACES)
        ]


class Scene:
    def __init__(self, scene_root_node):
        self.root_node = scene_root_node
        self.number = self.get_number()
        self.lines = self.get_lines()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.number})"

    def get_number(self):
        return int(self.root_node.get("n"))

    def get_lines(self):
        return [
            Line(line_root) for line_root in self.root_node.xpath(".//*[self::tei:l or self::tei:stage]", namespaces=NAMESPACES)
        ]


class Line:
    def __init__(self, line_root_node):
        self.root_node = line_root_node
        self.kind = self.get_kind()
        self.number = self.get_number()
        self.who = self.get_who()
        self.text = self.get_text()

    def __repr__(self):
        return f"{self.__class__.__name__}({self.text})"

    def get_kind(self):
        root_node_tag = etree.QName(self.root_node).localname
        if root_node_tag == "l":
            return "speech"
        elif root_node_tag == "stage":
            return "direction"
        else:
            raise ValueError(f"Unexpected line root_node tag: {self.root_node.tag}")

    def get_number(self):
        if self.kind == "direction":
            return None
        else:
            _, line_number = self.root_node.get("n").rsplit(".", 1)
            return int(line_number)

    def get_who(self):
        if self.kind == "direction":
            return self.root_node.get("who")
        else:
            speaker_node = self.root_node.xpath(
                "./ancestor::tei:sp", namespaces=NAMESPACES
            )
            assert len(speaker_node) == 1
            return speaker_node[0].get("who")

    def get_text(self):
        return "".join(self.root_node.xpath("./descendant::*/text()"))
