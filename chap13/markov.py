"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

Modified by Aliesha Garrett

"""

import string
import random

d={}
prefix=()

def process_file(filename, num=2):
    """Does Markov analysis on a file.

    filename: string
    num: integer, number of words in the "prefix"
   
    Returns: map from each prefix to possible suffixes.
    """
    
    fp = file(filename)
    skip_gutenberg_header(fp)

    for line in fp:
        for word in line.rstrip().split():
            process_word(word,num)


def skip_gutenberg_header(fp):
    """Reads from fp until it finds the line that ends the header.

    fp: open file object
    """
    for line in fp:
        if line.startswith('*END*THE SMALL PRINT!'):
            break


def process_word(word, num=2):
    """Processes each word

    word: string
    num: int
    Stores words and eventually adds entries to a dictionary.
    """
    global prefix
    if len(prefix) < num:
        prefix += (word,)
        return
    
    if prefix in d:
        d[prefix].append(word)
    else:
        d[prefix]=[word]
   
    prefix=shift(prefix,word)



def shift(t,word):
    """Makes a new prefix tuple by removing the first element and adding a new word to the end.

    t: tuple of strings
    word: string
    """

    return t[1:] + (word,)    




def generate_text(n=100):
    """Using Markov analysis generates a block of text n words long based on the given text."""


    first=random.choice(d.keys())
    statement=''
    for i in range(n):
        suffix = d.get(first, None)
        if suffix == None:
            random_text(n-i)
            return

        word= random.choice(suffix)
        statement += ' '+word
        first = shift(first, word)

    print statement

def markov_generation(filename='',n=100, num=2, *args):

    process_file(filename, num)
    generate_text(n)


markov_generation('emma.txt')
