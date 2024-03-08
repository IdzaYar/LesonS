import string
def get_letters_between(min_letter, max_letter):
    letters = string.ascii_letters
    min_index = letters.index(min_letter)
    max_index = letters.index(max_letter)
    return letters[min_index:max_index + 1]
user_input = input("Введіть дві літери через дефіс: ")
min_letter, max_letter = user_input.split('-')
result = get_letters_between(min_letter, max_letter)
print(user_input + "-->" + result)