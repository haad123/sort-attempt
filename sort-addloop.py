lst = [3, 7, 4, 5, 2, 6, 1, 8, 10, 15, 9, 12, 14, 11, 13]

n = len(lst) - 1 
for k in range(n):
    a, b = lst.index(min(lst) + k), lst.index(lst[k])
    lst[a], lst[b] = lst[b], lst[a]
print(lst)