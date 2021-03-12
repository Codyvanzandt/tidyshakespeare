import pytest
import os
from lxml import etree
from src.constants import NAMESPACES
from src.data_classes import Play, Act, Scene, Line

# XML Roots

@pytest.fixture
def play_xml_path():
    return os.path.join("data", "xml", "a_midsummer_nights_dream.xml")

@pytest.fixture
def play_root(play_xml_path):
    return etree.parse(play_xml_path).getroot()


@pytest.fixture
def act_root(play_root):
    return play_root.xpath(
        ".//tei:div[@type = 'act' and @n = '1']", namespaces=NAMESPACES
    )[0]


@pytest.fixture
def scene_root(act_root):
    return act_root.xpath(
        ".//tei:div[@type = 'scene' and @n = '1']", namespaces=NAMESPACES
    )[0]


@pytest.fixture
def line_direction_root(scene_root):
    return scene_root.xpath(".//tei:stage", namespaces=NAMESPACES)[0]


@pytest.fixture
def line_root(scene_root):
    return scene_root.xpath(".//tei:l", namespaces=NAMESPACES)[0]


# Data Classes


@pytest.fixture
def line(line_root):
    return Line(line_root)


@pytest.fixture
def line_direction(line_direction_root):
    return Line(line_direction_root)

@pytest.fixture
def scene(scene_root):
    return Scene(scene_root)

@pytest.fixture
def act(act_root):
    return Act(act_root)

@pytest.fixture
def play(play_root):
    return Play(play_root)