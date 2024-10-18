#List Methods
Numbers = [1,2,2,4,5,6,6,7]
uniques = []

for item in Numbers:
    if item not in uniques:
        uniques.append(item)
print(uniques)

