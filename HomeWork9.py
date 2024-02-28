import random
list1 = random.sample(range(1, 101), random.randint(3, 10))
list2 = [list1[0], list1[2], list1[-2]]
print("Початковий список:", list1)
print("Новий список:", list2)