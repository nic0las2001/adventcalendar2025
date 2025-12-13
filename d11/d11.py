from functools import cache
input = open("inputs/d11.txt","r")

directions = {}

for line in input:
    if len(line) > 1:
        initial, paths = line[:-1].split(": ")
        directions[initial] = paths.split(" ")

@cache # for directions
def path_find(ini, dac_seen, fft_seen, p2):
    c = 0
    if ini == "dac": dac_seen = True
    if ini == "fft": fft_seen = True 
    if ini == "out":
        if not p2 or (p2 and dac_seen and fft_seen):
            return 1
        else:
            return 0

    for node in directions[ini]:
        c += path_find(node, dac_seen, fft_seen, p2)
    return c

print("P1:", path_find("you", False, False, False))
print("P2:", path_find("svr", False, False, True))