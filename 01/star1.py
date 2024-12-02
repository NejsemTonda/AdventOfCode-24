import re
with open("input", 'r') as file:
    lines = list(file)

nums = [re.findall(r'\d+', row) for row in lines]

first = []
second = []
for f, s in nums:
    first.append(int(f))
    second.append(int(s))

first = sorted(first)
second = sorted(second)

res = 0
for f,s in zip(first, second):
    res += abs(f-s)



print(res)
