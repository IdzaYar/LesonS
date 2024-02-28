list1 = [8, 7, 9, 11, 5, 2]
if not list1:
    result = 0
else:
    sum1 = sum(list1[0::2])
    result = sum1 * list1[-1]
print(result)