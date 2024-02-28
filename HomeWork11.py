def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "На 0 ділити не можна!"
while True:
    number1 = float(input("Напишіть перше число: "))

    while True:
        oper = input("Введіть операцію (+, -, *, /): ")
        if oper in ('+', '-', '*', '/'):
            break
        else:
            print("Допустимі операції: +, -, *, /. Спробуйте ще раз.")

    number2 = float(input("Напишіть друге число: "))
    if oper == "+":
        result = add(number1, number2)
    elif oper == "-":
        result = subtract(number1, number2)
    elif oper == "*":
        result = multiply(number1, number2)
    elif oper == "/":
        result = divide(number1, number2)
    else:
        result = "невідома операція"
    print(f"Результат: {result}")
    input1 = input("Бажаєте продовжити (y/n): ").lower()
    if input1 != 'y':
        break