def word_count(str):
    count = dict()
    words = str.split()
    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1
    return
print(word_count(' the quick brown for jumps over the lazy dog'))
