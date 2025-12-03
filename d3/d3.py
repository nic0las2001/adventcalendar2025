def jolts_calculator(digits):
    input = open("inputs/d3.txt","r")
    jolts = []
    for line in input:
        if line[:-1].isnumeric():
            bank = [int(x) for x in line[:-1]]
            jolt = []
            max_indexes = [0]*digits

            for d in range(digits):
                max_digit = 0
                if d == 0:
                    init = 0
                else: 
                    init = max_indexes[d-1]+1

                final = len(bank)-digits+1+d

                for d2 in range(init, final):
                    if bank[d2] > max_digit:
                        max_digit = bank[d2]
                        max_index = d2
                jolt.append(str(max_digit))
                max_indexes[d] = max_index
            jolts.append(jolt)
    input.close()
    return sum([int("".join(jolts[i])) for i,_ in enumerate(jolts)])

print("P1:", jolts_calculator(2))
print("P2:", jolts_calculator(12))