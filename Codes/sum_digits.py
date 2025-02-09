#  Sum of Digits Until Single Digit
# Test Case = 67 => 6+7 = 13 => 1=3 => 4

def sum_num(num_list):
    add = 0
    for i in num_list:
        add += int(i)
    return add

def split_num(num):
    num_list = list(str(num))
    if len(num_list) > 1:
        split_sum = sum_num(num_list)
        return split_num(split_sum)
    else:
        return num


num = int(input("Enter num: \n"))
print(split_num(num))
