import json

import jsonpath


def read_json_data(file_path, locator_name):
    f = open(file_path)
    response = json.loads(f.read())
    value = jsonpath.jsonpath(response, locator_name)
    return value[0]
