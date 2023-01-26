import sys
from collections import Counter


def cardninality_items(filename):
    f = open(filename)
    s = set()
    for line in f.readlines():
        arr = line.split(',')
        for item in arr:
            s.add(item.strip())

    return len(s)

def all_itemsets(filename):
    f = open(filename)
    s = set()
    # dedup through set
    for line in f.readlines():
        arr = line.split(',')
        for item in arr:
            s.add(item.strip())
    ret = []
    # sort to make sure the set is uniq
    sl = sorted(list(s))

    for e in sl:
        s = set()
        s.add(e)
        t = [s]
        for item in ret:
            new = set.copy(item)
            new.add(e)
            t.append(new)

        ret += t

    return ret

def prob_S(si, data):
    # transform set to tuple as set is not hashable
    new_data = [tuple(d) for d in data]

    # calculate the occurrence with Counter
    counters = Counter(new_data)
    return counters[tuple(si)]/float(len(data))


filename = sys.argv[1]
print(cardninality_items(filename))
sets = all_itemsets(filename)
se = set()
se.add('bread')
se.add('cheese')
print(prob_S(se, sets))
