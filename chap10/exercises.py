"""Solutions to exercises 10.1 and 10.3 from Think Python.
Author:Aliesha Garrett
"""

def nested_sum(l):
    """Takes a list of numbers and returns their sum."""
    total=0
    for n in l:
        if type(n)==int:
            total += n
        if type(n)==list:
            total += nested_sum(n)
    return total





def cumulative_sum(l):
    """Takes a list of numbers of length n and returns a new list of length n where each element is the sum of the first list through the current element index."""
    res=[]
    total=0
    for n in l:
        if type(n) == list:
            total += nested_sum(n)
        if type(n) == int:
            total += n
        res.append(total)
    return res



def remove_duplicates(l):
    """Takes a list and returns a new list with only unique elements."""
    res=[]
    for i in range(len(l)):
        if l[i] not in res:
            res.append(l[i])
    return res
    


l=[555,0,1,2,2,2,3,4]
print remove_duplicates(l)
