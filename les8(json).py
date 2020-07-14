import json
from counter_of_words import simple_making, made_by_counter, made_by_re_counter


def open_file():
    with open("files/newsafr.json", encoding='utf-8') as f:
        json_data = json.load(f)

    news_list = json_data["rss"]["channel"]["items"]
    description_list = []
    for news in news_list:
        description_list.append(news["description"])

    return description_list


simple_making(open_file())
print('=' * 100)
made_by_counter(open_file())
print('=' * 100)
made_by_re_counter(open_file())
