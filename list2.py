def move_last_to_first(my_list):
    if len(my_list) > 1:
        last_element = my_list.pop()
        my_list.insert(0, last_element)
list1 = [24, 17, 9, 13]
move_last_to_first(list1)
print(list1)
list2 = [1]
move_last_to_first(list2)
print(list2)
list3 = []
move_last_to_first(list3)
print(list3)
list4 = [42, 13, 1, 19, 78]
move_last_to_first(list4)
print(list4)