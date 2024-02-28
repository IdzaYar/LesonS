import string
def hashtag(input_str):
    words = input_str.split()
    words1 = [word.strip(string.punctuation).capitalize() for word in words if not word.isdigit()]
    hashtag1 = ''.join(words1)
    hashtag1 = hashtag1[:140]
    return f"#{hashtag1}"
input1 = input("Введіть рядок: ")
result = hashtag(input1)
print(result)