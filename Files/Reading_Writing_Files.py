
def main():
    # open a file for writing and create it if it does not exist
    f = open("text_file.txt", "w+")

    # write some lines of data to the file
    for i in range(10):
        f.write("This is line " + str(i) + "\r\n")

    # open the file for appending text to the end
    f = open("text_file.txt", "a")
    for i in range(10, 20):
        f.write("This is another line " + str(i) + "\r\n")

    # Open the file back up and read the contents
    # check if the file successfully opened
    f = open("text_file.txt", "r")
    if f.mode == 'r':
        contents = f.read()
        print(contents)

    # another way to read file
    f = open("text_file.txt", "r")
    if f.mode == 'r':
        fl = f.readlines()
        for x in fl:
            print(x)

    # close the file when done
    f.close()


if __name__ == '__main__':
    main()
