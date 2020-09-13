import matplotlib.pyplot as plt
from date_utility import get_now_string, iso_to_datetime, range_date
from schedules import get_schedule_dict, is_nap_only
from io_utility import read_json, write_json

NAP_ONLY_LIMIT = 172800  # 48h
SCHEDULE_LIMIT = 864000  # 10j


def make_graph(data):
    dates = range_date(iso_to_datetime(data['start_date']),
                       iso_to_datetime(data['end_date']))
    _, ax = plt.subplots()
    ax.set_xlabel('date')
    ax.set_ylabel('number of attemp')
    ax.set_title(data['title'] if 'title' in data else 'title go brrr')
    mod = 'normal'
    for sch in data['value']:
        data_sch = [sum([data['value'][sch][j][i] for j in data['value'][sch]])
                    for i in range(len(data['value'][sch][mod]))]
        ax.plot(dates, data_sch, label=sch)
    ax.legend()
    plt.show()


def make_range_array(data, start_date='2017-05-07T00:15:38.541Z',
                     end_date=get_now_string(), count_adapted=True,
                     count_attempted=True):
    """
    create an array of dictionnary. Each cell represent one day, starting from
    the start_date to the end_date. Dictionnary schema:
    {schedule: {modifiers: number of attempt}}
    """
    start_dt = iso_to_datetime(start_date)
    end_dt = iso_to_datetime(end_date)
    delta = (end_dt - start_dt).days + 1
    res = get_schedule_dict(lambda: [0] * delta)
    if delta >= 2:
        for schedule in data:
            is_NO = is_nap_only(schedule)
            for modifier in data[schedule]:
                tmp_array = data[schedule][modifier]
                i = 0
                while (i < len(tmp_array) and tmp_array[i][0] < end_date):
                    attempt = tmp_array[i]
                    start_at = iso_to_datetime(attempt[0])
                    end_at = iso_to_datetime(attempt[1])
                    delta_attempt = end_at - start_at
                    in_range = (start_dt <= start_at <= end_dt) \
                        or (start_dt <= end_at <= end_dt) \
                        or (start_at <= start_dt and end_at >= end_dt)
                    delta_sec = delta_attempt.total_seconds()
                    valid_schedule = (delta_sec > SCHEDULE_LIMIT
                                      or (delta_sec > NAP_ONLY_LIMIT
                                          and is_NO))
                    adapted = attempt[2]
                    if in_range and valid_schedule \
                       and ((adapted and count_adapted)
                            or (not(adapted) and count_attempted)):
                        first = max((start_at - start_dt).days, 0)
                        last = delta - max(0, (end_dt - end_at).days)
                        for j in range(first, last):
                            res[schedule][modifier][j] += 1
                    i += 1
    else:
        raise Exception('Invalid range')
    return {'start_date': start_date, 'end_date': end_date, 'value': res}


def main():
    """
    main function for testing
    """
    data = read_json('../data/data_discord_format.json')
    data_to_plot = make_range_array(data, count_adapted=True,
                                    count_attempted=True)
    write_json(data_to_plot, name='../data/data_discord_to_plot.json')
    make_graph(data_to_plot)


if __name__ == '__main__':
    main()
