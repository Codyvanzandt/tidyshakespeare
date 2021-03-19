from lxml import etree
from src.preprocessing import change_line_breaks_to_spaces, preprocess_play
from src.constants import NAMESPACES


def test_change_line_breaks_to_spaces(fake_xml_root):
    change_line_breaks_to_spaces(fake_xml_root)
    break_container = fake_xml_root.xpath("./tei:A", namespaces=NAMESPACES)[0]
    assert etree.QName(break_container.getchildren()[0]).localname == "c"
    assert fake_xml_root.xpath(".//tei:lb", namespaces=NAMESPACES) == list()


def test_preprocess_play(fake_xml_root):
    preprocess_play(fake_xml_root)
    assert True
