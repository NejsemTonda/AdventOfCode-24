import re

res = 0
for s in re.findall(r'mul\(\d{1,3},\d{1,3}\)', open("input").read()):
    x,y = re.findall(r'\d+', s)
    res += int(x)*int(y)

print(res)
