class Mem():
    def __init__(self, pos, l):
        self.pos = pos
        self.l = l

    def val(self):
        return (2*self.pos + self.l-1) * self.l // 2


pos, mem = 0, []
for l in map(int, open('input').read().strip()):
    mem += [Mem(pos, l)]
    pos += l


for used in mem[::-2]:
    for free in mem[1::2]:
        if (free.pos <= used.pos and free.l >= used.l):
            used.pos = free.pos
            free.pos += used.l
            free.l -= used.l

print(sum(id*m.val() for id, m in enumerate(mem[::2])))
