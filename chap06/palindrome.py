"""Module that provides is_palindrome.

Author of is_palindrome: Aliesha Garrett
"""

def first(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[0]


def last(word):
    """Returns the first character of a word.

    word: string

    returns: length 1 string
    """
    return word[-1]


def middle(word):
    """Returns all but the first and last character of a word.

    word: string

    returns: string
    """
    return word[1:-1]




   

def is_palindrome(word):

	if first(word)!=last(word):
		return False
	elif middle(word)=='':
		return True
	else:
		new=middle(word)
		return is_palindrome(new)
"""This function takes a word and returns "True" if it is a palindrome and "False" if it is not.

word: string"""
  





