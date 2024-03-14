def correct_sentence(text):
    if not text.endswith('.'):
        text = text.capitalize() + '.'
    else:
        text = text.capitalize()
    words = text.split()
    for i in range(len(words)):
        if i > 0 and words[i - 1].endswith('.'):
            words[i] = words[i].capitalize()
    return ' '.join(words)
input_text = input("Введіть речення: ")
result = correct_sentence(input_text)
print("Результат:", result)