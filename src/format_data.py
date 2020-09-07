import json
import datetime
from utility import read_json, write_json
from schedules import get_schedule_dict


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
    tmp = schedule_name.split('-')
    if len(tmp) == 1:
        tmp.append('normal')
    return tmp


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
                schedule, modifier = cut_modifier(val['name'])
                new_obj[schedule][modifier].append([start, end, adapted])
    return new_obj


def main():
    data = read_json()
    new_data = format_data(data)
    write_json(new_data)


if __name__ == '__main__':
    main()
