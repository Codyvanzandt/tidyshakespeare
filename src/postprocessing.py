import re
from lxml import etree
from src.constants import NAMESPACES
from collections import Counter

def postprocess_play(play_data):
    play_data = list(remove_empty_text(play_data))
    play_data = list(add_throughline_numbers(play_data))
    play_data = list(parse_names(play_data))
    return play_data

def remove_empty_text(play_data):
    return filter(lambda x: x["text"], play_data)

def add_throughline_numbers(play_data):
    for i, line in enumerate(play_data):
        line["number"] = i+1
    return play_data

def parse_names(play_data):
    for line in play_data:
        if line["who"]:
            line["who"] = ",".join( parse_name(name) for name in line["who"].split() )
    return play_data

def parse_name(name): 
    return re.match(r"#?(.*)", name).group(1)
    







