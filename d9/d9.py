input = open("inputs/d9.txt","r")
from math import prod

red_tiles = []
for line in input:
    if len(line) > 1:
        red_tiles.append([int(x) for x in line[:-1].split(",")])

square_data = []
for tile1 in red_tiles:
    for tile2 in red_tiles:
        if tile1 == tile2: break
        else:
            distances = (abs(tile1[0]-tile2[0]) + 1, abs(tile1[1]-tile2[1]) + 1)
            square_data.append([tuple(tile1), tuple(tile2), distances, prod(distances)])

square_data = sorted(square_data, key=lambda y: y[3])[::-1]
print("P1:", square_data[0][3])

for square in square_data:
    c1, c2 = square[0:2]
    candidate = True
    # case 1: if a node is in a middle of the square then condition breaks
    for tile in red_tiles: 
        if tile[0] < max(c1[0], c2[0]) and tile[0] > min(c1[0], c2[0]):
            if tile[1] < max(c1[1], c2[1]) and tile[1] > min(c1[1], c2[1]):
                candidate = False
                break
    # case 2: borders going through partially/fully the square
    for ii, tile2 in enumerate(red_tiles): 
        if ii == len(red_tiles)-1:
            tile3 = red_tiles[0]
        else:
            tile3 = red_tiles[ii+1]
        if tuple(tile2) in square[0:2] or tuple(tile3) in square[0:2]:
            pass
        else:
            #horizontal
            if max(tile2[0], tile3[0]) >= max(c1[0], c2[0]) and min(tile2[0], tile3[0]) <= min(c1[0], c2[0]):
                if max(tile2[1], tile3[1]) <= max(c1[1], c2[1]) and min(tile2[1], tile3[1]) >= min(c1[1], c2[1]):
                    candidate = False 
                    break
            #vertical
            if max(tile2[1], tile3[1]) >= max(c1[1], c2[1]) and min(tile2[1], tile3[1]) <= min(c1[1], c2[1]):
                if max(tile2[0], tile3[0]) <= max(c1[0], c2[0]) and min(tile2[0], tile3[0]) >= min(c1[0], c2[0]):
                    candidate = False 
                    break
    if candidate:
        print("P2:", square[3])
        break