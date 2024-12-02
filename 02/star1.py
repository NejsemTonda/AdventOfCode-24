with open('input', 'r') as file:
    lines = list(file)

lines = [list(map(int, line.split())) for line in lines]

safe_lines = 0
for line in lines:
    safe = True
    dec = line[0] > line[1]
    for x,y in zip(line, line[1:]):
        if (not 1 <= abs(x-y) <= 3) or ((x<y and dec) or (x>y and not dec)):
            safe = False
            break

    if safe:
        safe_lines += 1

print(safe_lines)
