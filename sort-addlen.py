# Changes
    # assigned n variable to lst length to allow n recursion 
    
lst = [3, 7, 4, 5, 2, 6, 1]
# Task:
    # print lowest value in integer list 
    # print highest value in integer list
# sort the given list and print it      

print(min(lst)) # output 1, 1 is at index 6 initially
print(max(lst)) # output 7, 7 is at index 2 initially

print(len(lst)) # outputs 7
print(len(lst) - 1) # outputs 6 
    # n needs to be assigned to len(lst) - 1 not just len(lst);
        # n = len(lst) when used in min(lst) + 1 would be equal to 8 which is out of lst range

n = len(lst) - 1 # n = 6 
print(n)
for k in range(n):
    a, b = lst.index(min(lst) + k), lst.index(lst[k])
    lst[a], lst[b] = lst[b], lst[a]
    # theoretical output (n = 6): [3, 1, 4, 5, 2, 6, 7]
print(lst)
 
