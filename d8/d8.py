from math import sqrt
input = open("inputs/d8.txt","r")

junction_boxes = []
for line in input:
    if len(line) > 1:
        junction_boxes.append([int(x) for x in line[:-1].split(",")])

n_box = len(junction_boxes)
dist_grid = []

for idx1, box1 in enumerate(junction_boxes):
    dist_dic = {}
    for idx2, box2 in enumerate(junction_boxes):
        pair_dist = sqrt((box2[0]-box1[0])**2+(box2[1]-box1[1])**2+(box2[2]-box1[2])**2)
        if idx1-idx2 == 0:
            break
        else: 
            dist_dic[idx2] = pair_dist
    dist_grid.append(dist_dic)

circuits = []
connected = set()
for _ in range(1000):
    # find min circuit
    min = 0
    for n, node in enumerate(dist_grid):
        for key, val in node.items():
            if min == 0: 
                min = (n, key, val)
            elif val < min[2]:
                min = (n, key, val)
    if min != 0: 
        c1 = -1; c2 = -1
        for c_id, circuit in enumerate(circuits):
            if min[0] in circuit:
                c1 = c_id
            if min[1] in circuit:
                c2 = c_id
        if c1 >= 0 and c2 >= 0:
            if c1 == c2:
                pass
            else: 
                circuits[c1].update(circuits[c2])
                del circuits[c2]
        elif c1 >= 0:
            circuits[c1].add(min[1])
        elif c2 >= 0:
            circuits[c2].add(min[0])
        else:
            circuits.append({min[0], min[1]})
        connected.update(min[:2])
        del dist_grid[min[0]][min[1]]

circuits.sort(key = len, reverse = True)
prod = 1
for i in range(3):
    prod*= len(circuits[i])
print(prod)


