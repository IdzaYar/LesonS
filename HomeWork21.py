def popular_words(text, words):
    text_words = text.lower().split()
    word_count = {}
    for word in words:
        word_lower = word.lower()
        count = text_words.count(word_lower)
        word_count[word] = count
    print("Вихідні параметри:", word_count)
    return word_count
assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''',
                     ['i', 'was', 'three', 'near']) == {'i': 4, 'was': 3, 'three': 0, 'near': 0}, 'Test1'
print('OK')