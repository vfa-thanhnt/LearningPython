# Function with default argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return print(result)


# without param x which has default value of 1
power(9)
# change value of param x
power(7, 2)
# change the order of the params by supplying the names along with the values
power(x=3, num=2)


# Function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return print(result)


multi_add(2, 3, 4, 5, 10)


# Function with formal4 params and argument list
# Note: argument list should be the last param
def add_sub(a, b, *args):
    result = a + b
    for x in args:
        result = result - x
    return print(result)


add_sub(10, 20, 1, 2, 3, 4, 5)
