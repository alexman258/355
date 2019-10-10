#d1 = {'John': {'task1': 5},  'Rae': {'task1': 10, 'task2': 4},   
#    'Kelly': {'task1': 8, 'task3': 5},   'Alex': {'task1': 11, 
#    'task2': 2, 'task3': 1},  'Aaron': {'task2': 15}, 'Ethan':
#    'task3': 12}, 'Helen': {'task3': 10}}

def sprintLog(sprnt):
    d = {}
    for k,v in list(sprnt.items()):
        for t,h in list(v.items()):
            d[t] = d.get(t,{})
            d[t][k] = h
    return d


def lookupVal(L,k):
    for x in reversed(L):
        if x.get(k) is not None:
            return x.get(k)
    return None