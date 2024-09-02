def sum_maker(number_list):
    "Finds and retuns sum using list"
    list_sum = 0
    for num in number_list:
        list_sum += num
    return list_sum
    
print("sum of [4, 6, 7] is ", sum_maker([8, 5, 11]))