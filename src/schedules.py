import itertools

nap_only = ['Uberman', 'Dymaxion', 'Tesla', 'SPAMAYL', 'Naptation']
everyman = ['E2', 'E3', 'E4', 'E5', 'SEVAMAYL', 'Trimaxion']
biphasic = ['E1', 'Segmented', 'Siesta', 'BiphasicX']
dual_core = ['Bimaxion', 'DC1', 'DC2', 'DC3', 'DC4']
tri_core = ['TC1', 'TC2', 'Triphasic']
experimental = ['QC0', 'Experimental']
mono = ['Mono']
random = ['Random']
modifiers = ['shortened', 'extended', 'flipped', 'modified', 'recovery', 'normal']
    

def get_modifiers_list():
    return  {mod: [] for mod in modifiers}


def get_schedule_list_2d():
    """
    generate a list of list with the following format
    [[schedule name, schedule name, ...], [schedule name, ...], ...]
    each sub list being a type of sleep
    """
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
    return {sch: get_modifiers_list() for sch in tmp_list}
