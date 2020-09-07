import json
import datetime
import itertools
from utility import read_json, write_json

def get_schedule_list_2d():
    """
    generate a list of list with the following format
    [[schedule name, schedule name, ...], [schedule name, ...], ...]
    each sub list being a type of sleep
    """
    nap_only = ['Uberman', 'Dymaxion', 'Tesla', 'SPAMAYL', 'Naptation']
    everyman = ['E2', 'E3', 'E4', 'E5', 'SEVAMAYL', 'Trimaxion']
    biphasic = ['E1', 'Segmented', 'Siesta', 'BiphasicX']
    dual_core = ['Bimaxion', 'DC1', 'DC2', 'DC3', 'DC4']
    tri_core = ['TC1', 'TC2', 'Triphasic']
    experimental = ['QC0', 'Experimental']
    mono = ['Mono']
    random = ['Random']
    return list(itertools.chain.from_iterable([
        nap_only, everyman, biphasic, dual_core, tri_core, mono, experimental,
        random
    ]))


def get_schedule_dict():
    """
    return a dictionary. Schedma:
     {"schedule name": []}
    """
    tmp_list = get_schedule_list_2d()
    return {sch: [] for sch in tmp_list}


def iso_to_datetime(iso_date):
    """
    convert an ISO_8601 formatted string to a datetime object. Format of string
    is taken from JS date to string
    """
    return datetime.datetime.strptime(iso_date, '%Y-%m-%dT%H:%M:%S.%fZ')


def datetime_to_iso(date):
    """
    convert a datetime object to an ISO_8601 formatted string. Format of string
    is taken from JS date to string
    """
    return date.strftime('%Y-%m-%dT%H:%M:%S.%fZ')


def get_now_string():
    """
    return an ISO_8601 reprensentation of the actual time
    """
    return datetime_to_iso(datetime.datetime.now())


def cut_modifier(schedule_name):
    """
    cut the modifiers in the name, keeping only the schedule
    """
    return schedule_name.split('-')[0]


def format_data(obj):
    """
    read throught the data from napgod, and transform the dictionary of users
    to a dictionary. Schedma:
     {"schedule name": [[start, end]]}
    """
    new_obj = get_schedule_dict()
    now = get_now_string()
    for entry in obj:
        histo = entry['historicSchedules']
        for (i, val) in enumerate(histo):
            if i == (len(histo) - 1):
                end = now
            else:
                end = histo[i+1]['setAt']
                start = val['setAt']
                adapted = val['adapted']
                schedule = cut_modifier(val['name'])
                new_obj[schedule].append([start, end, adapted])
    return new_obj


def main():
    data = read_json()
    new_data = format_data(data)
    write_json(new_data)


if __name__ == '__main__':
    main()
