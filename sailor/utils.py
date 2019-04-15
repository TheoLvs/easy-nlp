

import json


def open_json_data(json_path,encoding = 'utf8'):
    return json.loads(open(json_path,"r",encoding = encoding).read())


def save_data_as_json(data,json_path,sort_keys = True):
    with open(json_path, 'w') as file:
        json.dump(data, file,indent = 4,sort_keys = sort_keys)


