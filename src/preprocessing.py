from lxml import etree
from src.constants import NAMESPACES

def preprocess_play(play_node):
    for func in (change_line_breaks_to_spaces,):
        play_node = func(play_node)
    return play_node

def change_line_breaks_to_spaces(play_node):
    for line_break in play_node.xpath("//tei:lb", namespaces=NAMESPACES):
        space = etree.fromstring("<c> </c>")
        line_break.getparent().replace(line_break, space)
    return play_node