__author__ = 'Raychang'

# Gnome Sort
def gnomesort(seq):
    i = 0
    while i < len(seq):
        if i == 0 or seq[i - 1] <= seq[i]:
            i += 1
        else:
            seq[i], seq[i - 1] = seq[i - 1], seq[i]
            i -= 1


seq = [1, 4, 51, 232, 3, 100, 23]
gnomesort(seq)
print seq


# Merge Sort
def mergesort(seq):
    mid = len(seq) // 2
    lft, rgt = seq[:mid], seq[mid:]
    if len(lft) > 1: lft = mergesort(lft)
    if len(rgt) > 1: rgt = mergesort(rgt)
    res = []
    while lft and rgt:
        if lft[-1] >= rgt[-1]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())
    res.reverse()
    return (lft or rgt) + res

seq1 = [1, 4, 51, 232, 3, 100, 24]
ret = mergesort(seq1)
print ret
