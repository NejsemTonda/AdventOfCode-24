with open('input', 'r') as file:
    lines = list(file)

lines = [list(map(int, line.split())) for line in lines]


def safe_level(line):
    dec = line[0] > line[1]
    for x,y in zip(line, line[1:]):
        if (not 1 <= abs(x-y) <= 3) or ((x<y and dec) or (x>y and not dec)):
            return False

    return True

safe_lines = 0
for line in lines:
    for i in range(len(line)):
        if safe_level(line[:i] + line[i+1:]):
            safe_lines += 1
            break

print(safe_lines)
