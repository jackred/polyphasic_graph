import requests
from io_utility import read_json, write_json


def get_json(url):
    """
    request the data from an url and read them as json
    """
    res = requests.get(url).json()
    return res


def get_json_from_config_url(field):
    """
    get the data from an url stored in the configuration file
    """
    config = read_json("../config.json")
    return get_json(config[field])


def get_json_report():
    """
    get the data from the url store in with the 'url_report' key
    in the configuration file
    """
    return get_json_from_config_url('url_report')


def get_json_report_discord():
    """
    get the data from the url store in with the 'url_report_discord' key
    in the configuration file
    """
    return get_json_from_config_url('url_report_discord')


def main():
    """
    main function for testing
    """
    data = get_json_report_discord()
    write_json(data, '../data/data_discord.json')


if __name__ == '__main__':
    main()
