plan = list(map(list, open('input').read().split()))
DIRECTIONS = [(0,-1), (1,0), (0,1), (-1,0)]

facing = DIRECTIONS[0]

def move(plan, facing):
    row = [row for row in plan if '^' in row][0]
    x = row.index('^')
    y = plan.index(row)

    plan[y][x] = 'X'
    if not 0 <= y + facing[1] < len(row) and 0 < x + facing[0] < len(plan):
        return plan, facing

    while plan[y + facing[1]][x + facing[0]] == '#':
        facing = DIRECTIONS[(DIRECTIONS.index(facing) + 1)%len(DIRECTIONS)]

    plan[y + facing[1]][x + facing[0]] = '^'

    return plan, facing

while True:
    plan, facing = move(plan, facing)
    if len([row for row in plan if '^' in row]) == 0:
        break

print(sum(row.count('X') for row in plan))
