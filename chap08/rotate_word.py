""" Solution for exercise 8.12 from Think Python.

Author: Aliesha Garrett
"""

def rotate_word(s,i):
    """ 'Rotates' each letter in a word 'i' places. (Rotating a letter is shifting through the alphabet, wrapping around to the beginning again if necessary.)

    i: integer
    s: string
    """
    word=''
    if abs(i) > 26:
        i=i%26
    for char in s:
        old=ord(char)
        new=old+i
        if old < 65:
            fixed=old
        elif old > 122:
            fixed=old
        elif 90 < old < 97:
            fixed=old
	elif 65 < old < 90:
            if new > 90:
                fixed=new-26
            elif new < 65:
                fixed=new+26
            else:
                fixed=new
        elif 97 < old < 122:
            if new > 122:
                fixed=new-26
            elif new < 97:
                fixed=new+26
            else:
                fixed=new
        rotated=chr(fixed)
        word=word+rotated
    return word

print rotate_word('cheer',7)
print rotate_word('melon',-10)
print rotate_word('sleep',9)
