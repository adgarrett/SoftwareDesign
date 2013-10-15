"""Solutions to Exercises 9.1-9.5 in Think Python.

Author: Aliesha Garrett, using starter code from Allen Downey
"""

def has_no_e(s):
    """ Takes a string s, returns a boolean indicating whether the string contains no e"""
    for char in s:
        if char == 'e':
             return False
    return True



def avoids(s,f):
    """Takes a string s and another string f. Returns bool True if s contains no characters in f and bool False if s contains any characters from f"""
    for char in s:
        if char in f:
            return False
    return True



def uses_only(s,f):
    """Takes two strings, s and f. Returns bool True if s contains only characters contained in f, and bool False if s contains any characters not contained in f."""
    for char in s:
        if char not in f:
            return False
    return True





def uses_all(s,f):
    """Takes two strings, s and f. Returns bool True if s uses all the characters contained in f. Returns bool False if f contains any characters not in s."""
    for char in f:
        if char not in s:
            return False
    return True


def main():
    for line in open('words.txt'):

        # remove whitespace from the beginning and end
        word = line.strip()

        if uses_all(word,'quizng'):
            print word


if __name__ == '__main__':
    main()
