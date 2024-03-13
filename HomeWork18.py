def common_elements():
    multiples3 = [i for i in range(1, 101) if i % 3 == 0]
    multiples5 = [i for i in range(1, 101) if i % 5 == 0]
    print("Список чисел, кратних 3:", multiples3)
    print("Список чисел, кратних 5:", multiples5)
    setmultiples3 = set(multiples3)
    setmultiples5 = set(multiples5)
    intersection_set = setmultiples3.intersection(setmultiples5)
    return intersection_set
result = common_elements()
print("Перетин множин:", result)