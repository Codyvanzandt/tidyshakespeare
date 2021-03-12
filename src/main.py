from lxml import etree
from src.data_classes import Play
from src.csv_generation import generate_csv

dream = Play(etree.parse("data/xml/a_midsummer_nights_dream.xml").getroot())

generate_csv(dream, "data/csv/a_midsummer_nights_dream.csv")