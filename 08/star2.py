plan = list(map(list, open('input').read().split()))

anthenas = {}
for y, row in enumerate(plan):
    for x, char in enumerate(row):
        if char == '.':
            continue 
        if char in anthenas:
            anthenas[char].append((x,y))
        else:
            anthenas[char] = [(x,y)]

for char in anthenas:
    for anthena1 in anthenas[char]:
        for anthena2 in anthenas[char]:
            if anthena1 == anthena2:
                continue
            dx, dy = (anthena2[0]-anthena1[0], anthena2[1]-anthena1[1])
            new_x, new_y = (anthena1[0] - dx, anthena1[1] - dy)
            plan[anthena1[1]][anthena1[0]] = '#'

            
            while 0 <= new_x < len(plan[0]) and 0 <= new_y < len(plan):
                if plan[new_y][new_x] == char:
                    new_x, new_y = (new_x - dx, new_y - dy)
                    continue

                plan[new_y][new_x] = '#'
                new_x, new_y = (new_x - dx, new_y - dy)




print('\n'.join(map(''.join, plan)))
print(sum(row.count('#') for row in plan))