def has_duplicates(t):
    return len(set(t)) != len(t)

def list_intersection(t1,t2):
    return list(set(t1)&set(t2))

def uses_only(word,s):
    return set(word) <= set(s)

def avoids(word,s):
    return set(word) & set(s) == set()



t1=[1,2,3,4,5,6,7]
t2=[1,1,1,1,1,6,7]
word='alphabet'
s1='alphbet'
s2='czqw'
s3='abcdefghijklmnopqrstuvwxyz'

print has_duplicates(t1)
print has_duplicates(t2)
print list_intersection(t1,t2)
print uses_only(word,s1)
print uses_only(word,s3)
print uses_only(word,s2)
print avoids(word,s2)
print avoids(word,s3)
print avoids(word,s1)
    
    
