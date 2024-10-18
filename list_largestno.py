#Python Program to find the largest no. in the list
Numbers = [1,2,37,45,98,23]
largest = Numbers[0]
for item in Numbers:
    if item> largest:
        largest = item
print(largest)
