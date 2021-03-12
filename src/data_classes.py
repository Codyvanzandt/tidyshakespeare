from lxml import etree
from src.constants import NAMESPACES

class Play:
    
    def __init__(self, play_root_node):
        self.root_node = play_root_node


class Act:
    
    def __init__(self, act_root_node):
        self.root_node = act_root_node


class Scene:
    
    def __init__(self, scene_root_node):
        self.root_node = scene_root_node


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
            speaker_node = self.root_node.xpath("./parent::tei:sp", namespaces=NAMESPACES)[0]
            return speaker_node.get("who")

    def get_text(self):
        return "".join( self.root_node.xpath("./descendant::*/text()") )