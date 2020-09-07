import requests
from io_utility import read_json, write_json


def get_json():
    config = read_json("../config.json")
    res = requests.get(config['url']).json()
    return res


if __name__ == '__main__':
    data = get_json()
    write_json(data, '../data/data.json')
