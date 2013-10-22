"""Solution for exercise 11.10 in Think Python.

Author: Aliesha Garrett"""


from rotate_word import rotate_word

def rotate_pairs(word_list):
    """Takes a word (string) and a word list (list of strings). Returns a dictionary where each key is a word and each value is a word it can rotate to create."""
    d=dict()
    res=dict()
    for word in word_list:
        d[word]=word
    for word in word_list:
        for i in range(1,26):
            rotated=rotate_word(word, i)
            if rotated in d:
                if word in res:
                    if type(res[word]) == str:
                        t=[res[word]]
                    else:
                        t=res[word]
                    t.append(rotated)
                    res[word]=t
                else:
                    res[word]=rotated
    return res




print rotate_pairs(['cheer','bunny','cubed','melon','jolly','diffs'])
    
