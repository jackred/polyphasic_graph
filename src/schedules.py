import itertools

schedules = {
    'nap_only' : ['Uberman', 'Dymaxion', 'Tesla', 'SPAMAYL', 'Naptation'],
    'everyman' : ['E2', 'E3', 'E4', 'E5', 'SEVAMAYL', 'Trimaxion'],
    'biphasic' : ['E1', 'Segmented', 'Siesta', 'BiphasicX'],
    'dual_core' : ['Bimaxion', 'DC1', 'DC2', 'DC3', 'DC4'],
    'tri_core' : ['TC1', 'TC2', 'Triphasic'],
    'experimental' : ['QC0', 'Experimental'],
    'mono' : ['Mono'],
    'random' : ['Random']
}
modifiers = ['shortened', 'extended', 'flipped', 'modified', 'recovery', 'normal']

def is_nap_only(sch):
    return sch in schedules['nap_only']


def get_modifiers_list(val):
    """
    generate a dictionnary. Schema:
    {modifiers: value}
    """
    return {mod: val() for mod in modifiers}


def get_schedule_list():
    """
    generate a list of list with the following format
    [schedule name, schedule name, ...]
    """
    return list(itertools.chain.from_iterable(schedules.values()))


def get_schedule_dict(val):
    """
    return a dictionary. Schema:
     {"schedule name": {modifiers: value}}
    """
    tmp_list = get_schedule_list()
    return {sch: get_modifiers_list(val) for sch in tmp_list}


def split_schedule(schedule_name):
    """
    split the schedule and the modifier
    """
    tmp = schedule_name.split('-')
    if len(tmp) == 1:
        tmp.append('normal')
    return tmp
