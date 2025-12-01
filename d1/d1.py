import re

input = open("d1/d1.txt","r")

dial = 50
zero_count = 0
passes_zero = 0

for line in input:
    if not line[0].isalpha():
        break
    direction = line[0]
    value = int(re.findall(r"\d+", line)[0])
    
    # handle spinning direction
    if direction == "L":
        value *= -1

    prev_dial = dial
    dial += value

    n_passes = abs(dial//100)
    # Part 1
    if dial%100 == 0:
            zero_count +=1 

    # Part 2 
    passes_zero += n_passes 

    #avoid double counting going from 0 to neg number 
    if prev_dial == 0 and dial < 0:
        passes_zero -= 1
    #account for extra count if going into negatives and finishing on 0
    if dial%100 == 0 and (prev_dial-dial) > 0:
        passes_zero += 1

    dial = dial%100

print(f"Landed on zero {zero_count} times (p1), landed + passed zero {passes_zero} times (p2).")