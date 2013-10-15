"""Solution to Exercise 10.12 from Think Python. Finds reverse pairs from words.txt

Author: Aliesha Garrett
"""

from bisect import bisect_left


def reverse_pairs(w_list):
    """Finds all reverse pairs in a sorted list.
    w_list:list of strings
    returns: list of lists containing pairs of strings"""

    res=[]
    for word in w_list:
        search=word[::-1]
        if in_list(w_list,search):
            res += [[word,search]]
    return res


def in_list(w_list,word):
    """Checks if a word is in a sorted list.
    list: list of strings
    word: string"""

    i=bisect_left(w_list,word)
    if i != len(w_list):
        if w_list[i] == word:
            return True
    return False


def make_word_list2():
    """Reads lines from a file and builds a list using list +.

    returns: list of strings
    """
    t = []
    for line in open('words.txt'):
        word=line.strip()
        t += [word]
    return t


w_list=make_word_list2()

print reverse_pairs(w_list)
