
def main():
    x = 0

    # while loop
    while x < 5:
        print(x)
        x = x + 1

    # for loop (start from 5 and end with 9)
    for i in range(5, 10):
        print(i)

    # loop for over a collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for i in days:
        print(i)

    # use break and continue statements
    # break: stop the loop
    # continue: skip current loop, continue to execute the next loop
    for x in range(10, 25):
        if x == 20:
            break
        if x % 2 == 0:
            continue
        print(x)

    # using enumerate() function to get index
    # enumerate return the index and the values of the collection
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    for index, value in enumerate(days):
        print(index, value)


if __name__ == '__main__':
    main()
