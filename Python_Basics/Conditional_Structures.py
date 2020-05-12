
def main():
    x, y = 3, 4

    if x > y:
        st = "x is greater than y"
    elif x > 2:
        st = "x is greater than 2"
    elif x == y:
        st = "x is equal to y"
    else:
        st = "x is less than y"

    print(st)

    # Conditional statements "a if c else b"
    a, b = 1, 2
    st = "a is greater than b" if (a > b) else "a is less than b"
    print(st)


if __name__ == '__main__':
    main()