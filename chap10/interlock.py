"""Solution to Exercise 10.13 from Think Python. Finds all interlocking word pairs in a list of words.

Author: Aliesha Garrett"""


from bisect import bisect_left


def interlock(w_list):
    """Finds all interlocking words in a sorted list. Returns a list of lists where the internal lists contain the two interlocking words and the word they form."""
    res=[]
    for word in w_list:
        if interlocked(w_list,word):
            res += [[word[::2],word[1::2],word]]
    return res






def interlocked(w_list, word):
    """Check if a word is made up of two different words from the list which are interlocked.
    w_list: list of strings
    word: string
    """
    evens = word[::2]
    odds = word[1::2]
    return in_list(w_list, evens) and in_list(w_list,odds)




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

print interlock(w_list)
