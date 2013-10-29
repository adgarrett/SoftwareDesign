"""This file contains solutions to exercises 14.1, 14.2 in Think Python.

Author: Aliesha Garrett
"""
import os
import sys
import anydbm
import pickle

def write_to_file():
    fout= open('output.txt','w')
    line1="This here's the wattle, \n"
    fout.write(line1)
    line2="the emblem of our land. \n"
    fout.write(line2)
    fout.close()

def i_spy(n,x,s):
    """Takes int n, floating point x, and string s. Prints a sentence."""
    print 'In %d minutes I have seen %g %s' % (n,x,s)


def databases():
    db=anydbm.open('captions.db', 'c')
    db['cleese.png']='Photo of John Cleese.'
    for key in db:
        print db[key]
    db.close()

def pickles():
    t=[1,2,3]
    print t
    s=pickle.dumps(t)
    print s
    t2=pickle.loads(s)
    print t2

def walk(directory):
    """Solution 14.1. Prints the names of all files in the given directory and its subdirectories.
    directory: string, name of a directory
    """

    for name in os.listdir(directory):
        path=os.path.join(directory,name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)


def sed(pattern, replace, file1, file2):
    """Solution 14.2. Reads file1, writes to file2. If pattern is found in file2, it is replaced with replace.

    pattern: string
    replace: string
    file1: string, filename
    file2: string, filename
    """

    try:
        fin = open(file1, 'r')
        fout = open(file2, 'w')

        for line in fin:
            line = line.replace(pattern, replace)
            fout.write(line)

        fin.close()
        fout.close()
    except:
        print 'There was an error.'



walk('.')

pattern='pattern'
replace='replace'
file1= 'text.txt'
file2= 'text_replaced.txt'
sed(pattern, replace, file1, file2)


