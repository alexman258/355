#d1 = {'John': {'task1': 5},  'Rae': {'task1': 10, 'task2': 4},   
#    'Kelly': {'task1': 8, 'task3': 5},   'Alex': {'task1': 11, 
#    'task2': 2, 'task3': 1},  'Aaron': {'task2': 15}, 'Ethan':
#    'task3': 12}, 'Helen': {'task3': 10}}
Aleksandr Mandzyuk
CptS 355
Assignment 3


# Dictionaries

def sprintLog(sprnt):
    d = {}
    for k,v in list(sprnt.items()):
        for t,h in list(v.items()):
            d[t] = d.get(t,{})
            d[t][k] = h
    return d

def addSprints(sprint1, sprint2):
    return None

def addNLogs(logList):
    return None


# Dictionaries and Lists

def lookupVal(L,k):
    for x in reversed(L):
        if x.get(k) is not None:
            return x.get(k)
    return None

def lookupVal2(tL,k):
    return None

def unzip(L):
    return None

def numPaths(m, n, blocks):
    return None

class iterFile():


def wordHistogram(words):
    return None