# **Write a Python function that takes a list and returns a new list with unique elements of the first list.**
#
#     Sample List : [1,1,1,1,2,2,3,3,3,3,4,5]
#     Unique List : [1, 2, 3, 4, 5]

def function_list(lst):
    unique_lst = []
    for i in lst:
        if i not in unique_lst:
            unique_lst.append(i)
    print(unique_lst)


function_list([1,1,1,1,2,2,3,3,3,3,4,5])