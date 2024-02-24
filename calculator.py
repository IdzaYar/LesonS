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
        return "на 0 ділити не можна!"
num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
operator = input("Введіть операцію (+, -, *, /): ")
if operator == '+':
    result = add(num1, num2)
elif operator == '-':
    result = subtract(num1, num2)
elif operator == '*':
    result = multiply(num1, num2)
elif operator == '/':
    result = divide(num1, num2)
else:
    result = "Невідома операція"
print("Результат:", result)