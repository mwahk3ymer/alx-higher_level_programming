#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5

    sum_result = add(a, b)
    diff_result = sub(a, b)
    prod_result = mul(a, b)
    div_result = div(a, b)

    print("{} + {} = {}".format(a, b, sum_result))
    print("{} - {} = {}".format(a, b, diff_result))
    print("{} * {} = {}".format(a, b, prod_result))
    print("{} / {} = {}".format(a, b, div_result))
