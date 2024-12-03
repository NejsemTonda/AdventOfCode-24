import re

res = 0
do = True
for s in re.findall(r"mul\(\d{1,3},\d{1,3}\)|do\(\)|don't\(\)", open("input").read()):
    
    if s == "don't()":
        do = False
    elif s == "do()":
        do = True
    elif do:
        x,y = re.findall(r'\d+', s)
        res += int(x)*int(y)

print(res)
