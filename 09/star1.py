disk_coding = open('input').read().strip()

disk = []
id_ = 0

# This could be more compact
for i in range(len(disk_coding)):
    if not i % 2:
        disk += [id_]*int(disk_coding[i])
        id_ += 1
    else:
        disk += ['.']*int(disk_coding[i])

while '.' in disk:
    tail = disk.pop()
    if tail == '.':
        continue
    disk[disk.index('.')] = tail #inefficeint, could just remeber the index here but I was lazy

print(sum(i*c for i,c in enumerate(disk)))
