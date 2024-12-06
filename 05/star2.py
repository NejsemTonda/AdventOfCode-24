lines = open('input').read().split()

rules = [line.split('|') for line in lines if '|' in line]
pages_list = [line.split(',') for line in lines if '|' not in line]


incorrect = []
for pages in pages_list:
    correct = True
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[0]) > pages.index(rule[1]):
                correct = False
    if not correct:
        incorrect.append(pages) 

well_reordered = []
while len(incorrect) > 0:
    pages = incorrect.pop(0)
    correct = True
    for rule in rules:
        if correct and rule[0] in pages and rule[1] in pages:
            i1 = pages.index(rule[0])
            i2 = pages.index(rule[1])
            if i1 > i2:
                pages[i1], pages[i2] = pages[i2], pages[i1]
                incorrect.append(pages)
                correct = False
    if correct:
        well_reordered.append(pages)

print(sum([int(p[len(p)//2]) for p in well_reordered]))
