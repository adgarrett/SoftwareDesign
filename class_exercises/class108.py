"""Class exercises for Software Design, October 8.
Author: Aliesha Garrett
"""

def singletnum(s):
    """Takes a string, s, and checks if it contains a single letter followed by a single number.
    """
    if len(s)!=2:
        return False
    elif 65 <= ord(s[0]) <= 90:
        return 48 <= ord(s[1]) <=57
    elif 97 <= ord(s[0]) <= 122:
        return 48 <= ord(s[1]) <=57
    else:
        return False

def letnum(s):
    """Takes a string, s, and checks if it is made up of any number of letters followed by any number of digits.
    """
    l=len(s)
    for i in range(l):
        if 48 <= ord(s[i]) <= 57:
            for n in range(l-i-1):
		a= s[n+i+1]
                if 48 > ord(a):
                    return False
                elif 57 < ord(a):
                    return False
    return True
            


def interleave(a,b):
    """Takes two strings and returns a new string which interleaves letters from the original two.
    """


    la=len(a)
    lb=len(b)
    string=''

    if abs(la-lb)>1:
       if la>lb:
           n=lb
       else:
           n=la
    elif la>lb:
           n=lb
    else:
           n=la

    for i in range(n):
           string=string+a[i]+b[i]

    if la>n:
       for i in range(la-n):
           string=string+a[i+n]

    if lb>n:
       for i in range(lb-n):
           string=string+a[i+n]

    return string


