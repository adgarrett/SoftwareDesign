def children(word):
    """Takes a string and returns a list of all strings which can be made by removing one character from the original string."""

    children=[]
    length=len(word)
    for i in range(length):
        child= word[:i]+word[i+1:]
        if child not in children:
            children.append(child)
    return children

def build_dictionary():
    """Builds a dictionary using words.txt where each key is a word and each value is the same word."""
    d=dict()
    for line in open('words.txt'):
        word=line.strip().lower()
        d[word]=word
    return d


def is_reducible(word,dictionary, reducible):
    """Takes a word, a dictionary with words as keys, and a dictionary with known reducible words as keys. Determines if the word is fully reducible. Returns a list where the 0th element is a boolean describing whether a word is fully reducible or not, and the 1th element is the dictionary of known reducible keys with any additions the function learns while checking the given word."""
    if word in dictionary:
        kids=children(word)
        if kids == []:
            return [True,reducible]
        else:
            reducible_child=[]
            for element in kids:
                if element in reducible:
                    return [True,reducible]
                reducible_child.append((element,is_reducible(element,dictionary,reducible)))
            for element in reducible_child:
                if element[1]:
                    add_word=element[0]
                    reducible[add_word]=add_word
                    return [True,reducible]
    else:
        return [False,reducible]


def find_reducible_words():
    reducible=dict()
    dictionary=build_dictionary()
    res=[]
    for word in dictionary:   
        check=is_reducible(word,dictionary,reducible)
        reducible=check[1]
        if check[0]:
            res.append((len(word),word))
    res.sort()
    return res



print find_reducible_words()
