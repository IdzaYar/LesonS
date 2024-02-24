def divide_list(input_list):
    length = len(input_list)
    if length == 0:
        return [[], []]
    middle = length // 2
    list1 = input_list[:middle + length % 2]
    list2 = input_list[middle + length % 2:]

    return [list1, list2]

list0 = []
result1 = divide_list(list0)
print(result1)

list3 = [1, 2, 3, 4, 5, 6]
result2 = divide_list(list3)
print(result2)

list4 = [1, 2, 3, 4, 5, 6, 7]
result3= divide_list(list4)
print(result3)