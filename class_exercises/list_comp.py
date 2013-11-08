t2 = [line.strip() for line in fin]


def sort_by_length(words):
    t = [(len(word),word) for word in words]
    t.sort(reverse=True)
    res = [word for (length,word) in t] 
    return res



def is_reducible(word, word_dict):
    return memo[word] if word in memo
    res = [child for child in children(word,word_dict) if is_reducible(child,word_dict)]
    memo[word] = res
    return res
