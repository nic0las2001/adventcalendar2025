import re
input = open("inputs/d2.txt","r")

all_IDs = [] 
invalid_IDs = []
invalid_IDs_p2 = []

for line in input:
    all_IDs.extend((re.split("-|\n",item) for item in line.split(",") if item[0].isnumeric()))

for ID_range in all_IDs:
    if ID_range[0].isnumeric():
        for ID in range(int(ID_range[0]),int(ID_range[1])+1):
            ID_str = str(ID)
            # Part 1
            half = int(len(ID_str)/2)
            if ID_str[0:half] == ID_str[half:]:
                invalid_IDs.append(ID)
            digits = list(ID_str)

            id_blacklist = [] # prevents single digit numbers to be added multiple times

            # Part 2
            for i in range(1, len(digits)):
                if len(digits) % i == 0:
                    test_case = []
                    for j in range((len(digits) // i)):
                        seq = ID_str[i*j:i*j+i]
                        if seq not in test_case:
                            test_case.append(ID_str[i*j:i*j+i])
                    if len(test_case) == 1 and ID not in id_blacklist:
                        invalid_IDs_p2.append(ID)
                        id_blacklist.append(ID)

print("P1: ", sum(invalid_IDs))
print("P2: ", sum(invalid_IDs_p2))