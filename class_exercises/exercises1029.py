def chronological(t):
    """Takes a list of strings containing dates in the format 'dd/mm/yyyy'. Returns a new list with the strings in chronological order."""
    t_sort=[]
    res=[]
    for s in t:
        tup=(s[4:],s[2:4],s[:2],s)
        t_sort.append((tup))
    t_sort.sort()
    for element in t_sort:
        res.append(element[3])
    return res


t=['01/05/1999','05/05/1999','01/05/1998','05/05/1998','06/05/1999']
#print chronological(t)


from swampy.Lumpy import Lumpy

lumpy = Lumpy()

prefix=('string1','string2')
new_prefix=(prefix[1:],'random_suffix')
d={}
d[prefix]=['suffix1','suffix2','suffix3']
d[new_prefix]=['suffix4','suffix5','suffix6']

def function(obj):
    lumpy.object_diagram()

function(d)
