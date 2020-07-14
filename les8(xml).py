import xml.etree.ElementTree as ET
from counter_of_words import simple_making, made_by_counter, made_by_re_counter


def open_file():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    items_list = root.findall("channel/item/description")
    description_list = []
    for description in items_list:
        description_list.append(description.text)
    return description_list


simple_making(open_file())
print('=' * 100)
made_by_counter(open_file())
print('=' * 100)
made_by_re_counter(open_file())
