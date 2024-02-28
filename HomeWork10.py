import string
import keyword


def name1(name):
    if name[0].isdigit():
        return False
    if name.isdigit():
        return False
    allowed_characters = string.ascii_lowercase + string.digits + "_"
    if any(char not in allowed_characters for char in name):
        return False
    if name in keyword.kwlist:
        return False
    return True
while True:
    input1 = input("Введіть назву змінної: ")
    print(name1(input1))