# Global variables in functions
f = 'test'


# if we do not declare variable as global variable inside function we basically use variable locally inside function
def print_variable():
    global f
    f = "abc"
    print(f)


# delete defined variable f so the variable f become undefined variable
del f

# If we do not declare variable f as global, the value of f shown using function will be different from print outside
print_variable()

# cannot show f since f is deleted above
# print(f)


