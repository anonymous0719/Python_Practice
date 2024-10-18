#Python Program to print F and L with loops
Numbers = [5,2,5,2,2]
for count_x in Numbers:
    print('x'* count_x)


for x_count in Numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)

Number = [2,2,2,2,8]
for count_x in Number:
    print('x'* count_x)