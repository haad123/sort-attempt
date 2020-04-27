# sort algorithm attempt 
# initial: [3, 7, 4, 5, 2, 6, 1]
# try to simplify algorithm with recursion
lst = [3, 7, 4, 5, 2, 6, 1]
# Task:
    # print lowest value in integer list 
    # print highest value in integer list
# sort the given list and print it      

print(min(lst)) # output 1, 1 is at index 6 initially
print(max(lst)) # output 7, 7 is at index 2 initially

a, b = lst.index(min(lst)), lst.index(lst[0])
    # lst[#] by itself just gives element value
        # lst.index(lst[#]) needs to be specified
    # lst.index should always be included;
        # otherwise, integer value of element is used as index, which us undesired
lst[a], lst[b] = lst[b], lst[a] # swaps the first element with the min element in lst
    # theoretical output: [1, 7, 4, 5, 2, 6, 3]

c, d = lst.index(min(lst) + 1), lst.index(lst[1])
    # c has index of sec_min element, d has index of second element
    # c has index 4, d has index 1 
        # output lst should be [1, 2, 4, 5, 7, 6, 3]
#print(lst.index(min(lst) + 1)) # output 4 because 2 is at 4th index position
lst[c], lst[d] = lst[d], lst[c] # swaps indicies
    # theoretical ouput: [1, 2, 4, 5, 7, 6, 3]

e, f = lst.index(min(lst) + 2), lst.index(lst[2])
lst[e], lst[f] = lst[f], lst[e]
    # theoretical ouput: [1, 2, 3, 5, 7, 6, 4]

h, i = lst.index(min(lst) + 3), lst.index(lst[3])
lst[h], lst[i] = lst[i], lst[h]
    # theoretical output: [1, 2, 3, 4, 7, 6, 5]

j, k = lst.index(min(lst) + 4), lst.index(lst[4])
lst[j], lst[k] = lst[k], lst[j]
    # theoretical output: [1,2, 3, 4, 5, 6, 7]

print(lst)
 
