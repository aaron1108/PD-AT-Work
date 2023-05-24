import json
from month_search import month_filter

if __name__ == '__main__':

    with open('dict_json.json', encoding='utf-8') as jsonfile:
        month = json.load(jsonfile)

    result = month_filter()

    result.search_condtion(month)