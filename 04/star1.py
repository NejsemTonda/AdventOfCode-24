cross_word = open('input').read().split()


def rotate(l):
    return [''.join(list(i)[::-1]) for i in zip(*l)]

def count_in_rows(cross_word):
    count = 0
    for row in cross_word:
        count += row.count("XMAS")

    return count

def count_diagonal(cross_word):
    xmas = "XMAS"
    count = 0
    for i1 in range(len(cross_word)-len(xmas)+1):
        for i2 in range(len(cross_word[0])-len(xmas)+1):
            for i,c in enumerate(xmas):
                if cross_word[i1+i][i2+i] != c:
                    break
            else:
                count += 1

    return count 

count = 0
for i in range(4):
    cross_word = rotate(cross_word)
    count += count_in_rows(cross_word)
    count += count_diagonal(cross_word)

print(count)
