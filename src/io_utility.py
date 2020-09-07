import json


def read_json(name='../data/data.json'):
    """
    read the data from a json file and decode them
    """
    with open(name, 'r') as mfile:
        data = mfile.read()
    # parse file
    obj = json.loads(data)
    return obj


def write_json(data, name='../data/data_format.json'):
    """
    write the formatted json data inside a file
    """
    with open(name, 'w') as mfile:
        json.dump(data, mfile)
