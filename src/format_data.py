from io_utility import read_json, write_json
from schedules import get_schedule_dict, cut_modifier
from date_utility import get_now_string


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
