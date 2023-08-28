#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    count = 0

    while count < list_length:
        try:
            dividend = my_list_1[count]
            divisor = my_list_2[count]

            if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                print("wrong type")
                result.append(0)
            elif divisor == 0:
                print("division by 0")
                result.append(0)
            else:
                result.append(dividend / divisor)
        except IndexError:
            print("out of range")
            result.append(0)

        count += 1

    return result
