f = open('three')
biome = [line.replace('\n', '') for line in f]

position_x = 0
right = 3
down = 1

counter = 0

for position_y in range(len(biome)):
    if biome[position_y][position_x] == "#":
        counter += 1
    position_x = (position_x + right) % len(biome[0])

print (counter)