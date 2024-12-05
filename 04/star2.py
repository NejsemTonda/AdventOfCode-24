cross_word = open('input').read().split()

def count_mas(i1, i2, cross_word):
    if cross_word[i1][i2] != "A":
        return 0
    count = 0
    if cross_word[i1+1][i2+1] == "M" and cross_word[i1-1][i2-1] == "S":
        count += 1

    if cross_word[i1-1][i2-1] == "M" and cross_word[i1+1][i2+1] == "S":
        count += 1

    if cross_word[i1+1][i2-1] == "M" and cross_word[i1-1][i2+1] == "S":
        count += 1

    if cross_word[i1-1][i2+1] == "M" and cross_word[i1+1][i2-1] == "S":
        count += 1

    return int(count > 1)


count = 0
xdim = len(cross_word[0])
ydim = len(cross_word)

for i1 in range(1,ydim-1):
    for i2 in range(1,xdim-1):
        count += count_mas(i1, i2, cross_word)

print(count)
