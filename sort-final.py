# Author: haad123
# Date: 28/4/2020

# add input for lst [pending]

# use initial [3, 7, 4, 5, 2, 6, 1] list when testing 
lst = [3, 7, 4, 5, 2, 6, 1, 8, 12, 10, 11, 9]
#_input = lst.split() 
    # .split() splits lst input into a list format 
# task is to allow input of a list of any length, sort, then print

n = len(lst) - 1 
for k in range(n):
    a, b = lst.index(min(lst) + k), lst.index(lst[k])
    lst[a], lst[b] = lst[b], lst[a]
print("Sorted: ",lst)