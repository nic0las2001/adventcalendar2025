input = open("inputs/d5.txt","r")

fresh_ranges = []
fresh_count = 0
for item in input:
    if "-" in item:
        range_str = item[:-1].split("-")
        range_num = (int(range_str[0]),int(range_str[1]))
        fresh_ranges.append(range_num)
    elif len(item) > 1:
        for IDs in fresh_ranges:
            if int(item) >= IDs[0] and int(item) <= IDs[1]:
                fresh_count += 1 
                break

print("P1:", fresh_count)

bounds = []
prev_bounds = fresh_ranges[:]
while bounds != prev_bounds: # might be smarter to sort list instead of while but this works also
    if bounds != []:
        prev_bounds = bounds[:]
    bounds = []
    for item in prev_bounds:
        if len(bounds) == 0:
            bounds.append(list(item))
        else:
            flag = True
            for bound in bounds:
                if item[0] >= bound[0] and item[0] <= bound[1] and item[1] > bound[1]:
                    bound[1] = item[1]
                    flag = False
                    break
                elif item[1] >= bound[0] and item[1] <= bound[1] and item[0] < bound[0]:
                    bound[0] = item[0]
                    flag = False
                    break
                elif item[0] <= bound[0] and item[1] >= bound[1]:
                    flag = False
                    bound[0] = item[0]
                    bound[1] = item[1]
                    break
                elif item[0] >= bound[0] and item[1] <= bound[1]:
                    flag = False
                    break
            if item not in bounds and flag:
                    bounds.append(list(item))
                
ID_count = 0
for item in bounds:
    ID_count += item[1] - item[0] +1

print("P2:", ID_count)