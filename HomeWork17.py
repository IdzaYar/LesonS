def correct_sentence(text):
    if not text.endswith('.'):
        text = text.capitalize() + '.'
    return text

# Введення речення від користувача
input_text = input("Введіть речення: ")
result = correct_sentence(input_text)
print("Результат:", result)