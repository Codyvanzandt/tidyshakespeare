import os
from lxml import etree
from src.data_classes import Play
from src.constants import NAMESPACES
from src.preprocessing import preprocess_play
from src.postprocessing import postprocess_play
from src.utils import read_play_csv, write_play_csv, get_play_data


def create_all_play_csv(input_dir, output_dir):
    for play_xml_file in os.listdir(input_dir):
        file_name, _ = play_xml_file.rsplit(".", 1)
        input_xml_path = os.path.join(input_dir, play_xml_file)
        output_csv_path = os.path.join(output_dir, file_name + ".csv")
        create_play_csv(input_xml_path, output_csv_path)


def create_play_csv(input_xml_path, output_csv_path):
    play_root = etree.parse(input_xml_path).getroot()
    preprocessed_play_root = preprocess_play(play_root)
    play_object = Play(preprocessed_play_root)
    play_data = get_play_data(play_object)
    postprocessed_play_data = postprocess_play(play_data)
    write_play_csv(postprocessed_play_data, output_csv_path)
