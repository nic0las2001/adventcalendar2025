import numpy as np
from functools import cache
input = open("inputs/d7.txt","r")

manifold = []
for line in input:
    if len(line)> 1:
        manifold.append([c for c in line[:-1]])

manifold = np.array(manifold)
start = np.where(manifold == "S")
start = (int(start[0][0]), int(start[1][0]))

beam_starts = {start[1]:1}
split_count = 0

for i in range(1,manifold.shape[0]):
    new_beams = []
    for beam in beam_starts.keys():
        if manifold[i, beam] == "^":
            if beam+1 not in new_beams:
                new_beams.append(beam+1)
            if beam-1 not in new_beams:
                new_beams.append(beam-1)
            split_count += 1
        else:
            if beam not in new_beams:
                new_beams.append(beam)
    beam_starts = {key:1 for key in new_beams}

print("P1:", split_count)

@cache # needed otherwise it would take ages to keep passing around the manifold
def beam_splitter(start):
    i, j = start 
    if i == manifold.shape[0]-1:
        return 1

    i += 1
    if manifold[i,j] == "^":
        return beam_splitter((i, j-1)) + beam_splitter((i, j+1))
    else:
        return beam_splitter((i,j))

print("P2:", beam_splitter(start))