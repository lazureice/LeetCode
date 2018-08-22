def uncommonFromSentences(A, B):
    """
    :type A: str
    :type B: str
    :rtype: List[str]
    """
    words = A.split() + B.split()
    words.sort()
    if len(words) < 2:
        return words

    length = len(words)
    i = 0
    res = []
    while i < length:
        if i == length-1:
            res.append(words[i])
            break
        if words[i] == words[i + 1]:
            while i < length - 1:
                if words[i] == words[i + 1]:
                    i += 1
                else:
                    break
        else:
            res.append(words[i])
        i += 1
    return res


A = "apple apple"
B = "banana"

res = uncommonFromSentences(A, B)

print(res)
