from io_utility import read_json, write_json
from schedules import get_schedule_dict, split_schedule
from date_utility import get_now_string


def format_data(obj):
    """
    read throught the data from napgod, and transform the dictionary of users
    to a dictionary. Schedma:
     {"schedule name": [[start, end]]}
    """
    new_obj = get_schedule_dict(list)
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
            schedule, modifier = split_schedule(val['name'])
            new_obj[schedule][modifier].append([start, end, adapted])
    for sch in new_obj:
        for mod in new_obj[sch]:
            new_obj[sch][mod].sort(key=lambda x: x[0])
    return new_obj


def main():
    """
    main function for testing
    """
    data = read_json('../data/data_discord.json')
    data2 = read_json('../data/data.json')
    new_data = format_data(data)
    new_data2 = format_data(data2)
    write_json(new_data, '../data/data_discord_format.json')
    write_json(new_data2, '../data/data_format.json')


if __name__ == '__main__':
    main()
