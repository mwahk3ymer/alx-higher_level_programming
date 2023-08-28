#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = []
    
    try:
        for i in range(list_length):
            try:
                dividend = my_list_1[i]
                divisor = my_list_2[i]

                if not isinstance(dividend, (int, float)) or not isinstance(divisor, (int, float)):
                    result.append(0)
                    print("wrong type")
                elif divisor == 0:
                    result.append(0)
                    print("division by 0")
                else:
                    result.append(dividend / divisor)
            except IndexError:
                result.append(0)
                print("out of range")
    except ZeroDivisionError:
        pass
    finally:
        return result
