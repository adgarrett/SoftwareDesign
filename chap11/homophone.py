"""Solution to Exercise 11.11 from Think Python.
Author: Aliesha Garrett"""

from pronounce import read_dictionary

def make_word_dict():
    """Reads words in words.txt and returns a dictionary with all words as keys."""
    d=dict()
    for line in open('words.txt'):
        word=line.strip().lower()
        d[word]=word
    return d

def homophones(a,b,d):
    """Determines if words a and b are homophones."""
    if a not in d or b not in d:
        return False
    return d[a]==d[b]
        
        

def find_homophones():
    """Finds words that solve the CarTalk riddle in exercise 11.11. Checks all words to see if removing their first letter results in a homophone, and if removing the second letter after returning the first results in a homophone. Result is a list of all qualifying words."""
    res=[]
    word_dict=make_word_dict()
    d=read_dictionary()
    for word in word_dict:
        word1=word[1:]
        if word1 in word_dict:
            if homophones(word,word1,d):
                word2=word[0]+word[2:]
                if word2 in word_dict:
                    if homophones(word,word2,d):
                        res.append(word)
    return res

print find_homophones()
