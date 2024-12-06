lines = open('input').read().split()

rules = [line.split('|') for line in lines if '|' in line]
pages_list = [line.split(',') for line in lines if '|' not in line]


result = 0
for pages in pages_list:
    correct = True
    for rule in rules:
        if rule[0] in pages and rule[1] in pages:
            if pages.index(rule[0]) > pages.index(rule[1]):
                correct = False
    if correct:
        result += int(pages[len(pages)//2]) 
print(result)
