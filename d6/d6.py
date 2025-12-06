import numpy as np
input = open("inputs/d6.txt","r")

data = []
aligned_data = []
for line in input:
    if len(line) > 1:
        data.append([int(x) if x.isnumeric() else x for x in line[:-1].split()])
        aligned_data.append(line[:-1])
operators = data[-1]
np_data = np.array(data[:-1])
aligned_data = aligned_data[:-1]

def sum_table(operators, np_data):
    column_resultants = []
    for idx, sign in enumerate(operators):
        if sign == "+":
            column_resultants.append(sum(np_data[:, idx]))
        elif sign == "*":
            # filtering 0s out to have the np array for p2
            prod = 1
            for n in np_data[:, idx]:
                if n != 0:
                    prod *= n
            column_resultants.append(prod)
    return sum(column_resultants)

print("P1: ", sum_table(operators, np_data))

i_max, j_max = len(aligned_data), len(aligned_data[0])
vert_unsorted = [""]*j_max
for i in range(i_max):
    for j in range(-1, -j_max-1,-1):
        vert_unsorted[abs(j)-1] += aligned_data[i][j]

vertical = []
sub = []
for item in vert_unsorted:
    numerical = False
    for c in item:
        if c.isdigit():
            numerical = True
    if numerical:
        sub.append(item)
    else:
        vertical.append(list(sub))
        sub = []
vertical.append(list(sub)) # last column is forgotten otherwise

l_max = 0
l_max = max([len(arr) for arr in vertical])

for arr in vertical:
    while len(arr) < l_max:
        arr.append(0) # need to expand some arrays to have homogeneous dimensions

vertical = np.array(vertical)
vertical = vertical.astype(int) # set array to integers
vertical = np.transpose(vertical)

print("P2: ", sum_table(operators[::-1], vertical))