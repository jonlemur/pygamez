myDict = [
    {'pos':(2,2),'cost':2},
    {'pos':(1,1),'cost':1},
    {'pos':(3,3),'cost':3},
    {'pos':(4,4),'cost':3}
]

costs = []
for tile in myDict:
    costs.append(tile['cost'])

costs.sort()
print(costs)

myDictSorted = []
for c in costs:
    for tile in myDict:
        if tile['cost'] == c:
            if tile not in myDictSorted:
                myDictSorted.append(tile)

print(myDictSorted)