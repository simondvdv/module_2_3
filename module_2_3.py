my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
my_list_index = 0
while my_list_index < len(my_list):
    if my_list[my_list_index] > 0:
        print(my_list[my_list_index])
    elif my_list[my_list_index] < 0:
        break
    my_list_index += 1
