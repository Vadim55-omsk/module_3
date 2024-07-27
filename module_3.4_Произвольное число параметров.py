def single_root_words(root_word, *other_words):
    same_words = []
    for i in other_words:
        if root_word.lower() in i.lower():
            same_words.append(i)
    for i in other_words:
        if i.lower() in root_word.lower():
            same_words.append(i)
    return same_words



result1 = single_root_words('кор', 'корень', 'корка', 'один', 'два')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
