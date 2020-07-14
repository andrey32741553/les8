from collections import Counter
import re


def simple_making(d_list):
    tmp_list = []
    for words in d_list:
        tmp_list.append(words.lower())
    tmp_list = ' '.join(tmp_list)
    description_dict = {}

    for word in tmp_list.split():
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
    tmp_list = []
    for words in d_list:
        tmp_list.append(words.lower())
    tmp_list = ' '.join(tmp_list)
    list_for_count = []
    for word in tmp_list.split():
        if len(word) > 5:
            list_for_count.append(word)
    counts = Counter(list_for_count)
    print(counts.most_common(10))


def made_by_re_counter(d_list):
    cnt_rus = Counter(x for x in re.findall(r'[А-я\']{6,}', str(d_list).lower()))
    cnt_eng = Counter(x for x in re.findall(r'[A-z\']{6,}', str(d_list).lower()))
    cnt = cnt_rus + cnt_eng
    print(cnt.most_common(10))
