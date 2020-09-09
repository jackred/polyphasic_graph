import datetime
from dateutil import rrule


# https://stackoverflow.com/a/11324695/8040287
def range_date(start, end):
    """
    return a list of date between start and end, included.
    """
    return list(rrule.rrule(rrule.DAILY,
                            count=(end-start).days + 1,
                            dtstart=start))


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
