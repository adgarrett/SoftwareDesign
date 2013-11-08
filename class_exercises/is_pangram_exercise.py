
import string

def uses_all(word, letters):
    for c in letters:
        if c not in word:
            return False
    return True


def is_pangram1(phrase):
    return uses_all(phrase.lower(), string.ascii_lowercase)


def is_pangram2(phrase):
    letterset = set(phrase.lower())
    letterset = letterset.difference(string.whitespace +
                                     string.punctuation)
    return len(letterset) == 26


def is_pangram3(phrase):
    letterset = set(phrase.lower())
    letterset -= set(string.whitespace + string.punctuation)
    return len(letterset) == 26


def is_pangram4(phrase):
    return set(string.ascii_lowercase).issubset(phrase.lower())


def is_pangram5(phrase):
    letters = phrase.lower().replace(' ', '')
    return len(set(letters)) == 26


def is_pangram6(phrase):
    phrase = phrase.lower()
    for c in string.ascii_lowercase:
        if c not in phrase:
            return False
    return True

phrase='The quick brown fox jumps over the lazy dog.'
print is_pangram1(phrase)
print is_pangram2(phrase)
print is_pangram3(phrase)
print is_pangram4(phrase)
print is_pangram5(phrase)
print is_pangram6(phrase)
phrase2='I am not a pangram.'
print is_pangram1(phrase2)
print is_pangram2(phrase2)
print is_pangram3(phrase2)
print is_pangram4(phrase2)
print is_pangram5(phrase2)
print is_pangram6(phrase2)
