import xml.etree.ElementTree as ET
from collections import Counter
import re


def open_file():
    parser = ET.XMLParser(encoding="utf-8")
    tree = ET.parse("files/newsafr.xml", parser)
    root = tree.getroot()
    items_list = root.findall("channel/item/description")
    description_list = []
    for description in items_list:
        description_list.append(description.text)
    return description_list


def simple_making(d_list):
    tmp_list = str(d_list).split()
    description_dict = {}

    for word in tmp_list:
        if word in description_dict:
            description_dict[word] += 1
        else:
            description_dict[word] = 1

    tmp_dict = {}
    for key, value in description_dict.items():
        if len(key) > 5:
            tmp_dict[key] = value

    result_dict = {}
    i = 0
    for key in sorted(tmp_dict, key=tmp_dict.get, reverse=True):
        result_dict[key] = tmp_dict[key]
        i += 1
        if i == 10:
            break
    print(result_dict)


def made_by_counter(d_list):
    tmp_list = str(d_list).split()
    list_for_count = []
    for word in tmp_list:
        if len(word) > 5:
            list_for_count.append(word)
    counts = Counter(list_for_count)
    print(counts.most_common(10))


def made_by_re_counter(d_list):
    cnt = Counter(x for x in re.findall(r'[А-я\']{6,}', str(d_list)))
    print(cnt.most_common(10))


simple_making(open_file())
print('=' * 100)
made_by_counter(open_file())
print('=' * 100)
made_by_re_counter(open_file())
