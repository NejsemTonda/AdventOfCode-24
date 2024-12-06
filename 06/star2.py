import copy

plan = list(map(list, open('input').read().split()))
DIRECTIONS = [(0,-1), (1,0), (0,1), (-1,0)]

facing = DIRECTIONS[0]

def move(plan, facing, pos):
    x,y = pos
    plan[y][x] = 'X'
    if not (0 <= y + facing[1] < len(plan) and 0 <= x + facing[0] < len(plan[0])):
        return plan, (0,0)

    while plan[y + facing[1]][x + facing[0]] == '#':
        facing = DIRECTIONS[(DIRECTIONS.index(facing) + 1)%len(DIRECTIONS)]

    plan[y + facing[1]][x + facing[0]] = '^'

    return plan, facing

def get_position(plan):
    row = [row for row in plan if '^' in row][0]
    x = row.index('^')
    y = plan.index(row)
    
    return x,y

def count_visited_squares(plan):
    return sum(row.count('X') for row in plan)


def get_stuck(plan, facing):
    states = set()
    x,y = get_position(plan)
    while True:
        if facing == (0, 0):
            return False
        
        state = (x,y,facing)
        if state in states:
            return True
        states.add((x,y, facing))

        plan, facing = move(plan, facing, (x,y))
        x,y = x+facing[0], y+facing[1]

stuck = 0
################
# No need to check all the positons. We can only check position visited without any new obstacle. But I was lazy to implement
###############k
for y in range(len(plan[0])):
    for x in range(len(plan)):
        new_plan = copy.deepcopy(plan)
        if new_plan[x][y] == '^':
            continue
        new_plan[x][y] = '#'
        
        if get_stuck(new_plan, facing):
            stuck += 1

