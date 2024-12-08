lines = [list(map(lambda x: int(x.replace(':', '')), line.split())) for line in open('input').read().split('\n')][:-1]


def compute(target, nums, ops):
    x = nums[0]
    for num, op in zip(nums[1:], ops):
        x = op(x,num)

    return x == target

def combinations(choices, n):
    if n == 1:
        return [[c] for c in choices]
    res = []
    prev = combinations(choices, n-1)
    for p in prev:
        for c in choices:
            res.append(p + [c])

    return res


plus = lambda x, y: x+y
mul = lambda x, y: x*y
con = lambda x,y: int(str(x) + str(y))

res = 0
for line in lines:
    target, *nums = line

    for op in combinations([plus, mul, con], len(nums)-1):
        if compute(target, nums, op):
            res += target
            break
    
print(res)
