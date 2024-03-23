def pow(x):
    return x ** 2
def some_gen(begin, end, func):
    """
    begin: перший елемент
    end: кількість елементів
    func: функція, яка формує значення
    """
    result = begin
    for _ in range(end):
        yield result
        result = func(result)
from inspect import isgenerator
gen = some_gen(2, 4, pow)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')