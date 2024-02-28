list1 = [1, 0, 2, 0, 3, 4, 0, 5]
for i in range(len(list1)):
    if list1[i] == 0:
        for j in range(i + 1, len(list1)):
            if list1[j] != 0:
                list1[i], list1[j] = list1[j], list1[i]
                break
print(list1)