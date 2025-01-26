def reverse_integer(num):
    if num < 0:
        num_reverse = -num

        # change num to string
        str_num = str(num_reverse)

        # reverse the number
        str_num = str_num[::-1]

        return -1 * int(str_num)
    else:
        num_reverse = num

        # change num to string
        str_num = str(num_reverse)

        # reverse the number
        str_num = str_num[::-1]

        return int(str_num)


print(reverse_integer(120))
