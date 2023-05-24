import json
import month_search

if __name__ == '__main__':

    with open('dict_json.json', encoding='utf-8') as jsonfile:
        month = json.load(jsonfile)

    result = month_search.month_filter()

    result.search_condtion(month)