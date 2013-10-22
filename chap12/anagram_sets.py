"""Solution to exercise 12.4 of Think Python.
Author: Aliesha Garrett
"""

def anagrams():
    """Reads words in words.txt and prints all the sets of words that are anagrams. Returns the dictionary in which the values are anagram sets and the keys are sorted tuples of the letters used to make an anagram. """
    d=dict()
    res=dict()
    sorted_res=[]
    bingo=[]
    for line in open('words.txt'):
        word=line.strip().lower()
        d[word]=word
    for key in d:
        word=list(key)
        word.sort()
        t=tuple(word)
        if t not in res:
            res[t]=[key]
        else:
            res[t].append(key)

    for key in res:
        if len(res[key])>1:
            sorted_res.append((len(res[key]),res[key]))
        if len(key)==8:
            bingo.append((len(res[key]),key))

    sorted_res.sort(reverse=True)
    bingo.sort(reverse=True)

    for element in sorted_res:   
        print element[1]
    
    print bingo[0][1]
    return res




anagrams()
