import os
from os import path
import datetime
from datetime import date, time, timedelta
import time


def main():
    # show the name of the OS
    print(os.name)

    # check for item existence and type
    print("Item exists: " + str(path.exists("text_file.txt")))
    print("Item is a file: " + str(path.isfile("text_file.txt")))
    print("Item is a directory: " + str(path.isdir("text_file.txt")))

    # work with file path
    print("Item path: " + str(path.realpath("text_file.txt")))
    print("Item path and name: " + str(path.split(path.realpath("text_file.txt"))))

    # Get the modification time
    t = time.ctime(path.getmtime("text_file.txt"))
    print(t)

    # another way to convert to date time with other format
    t2 = datetime.datetime.fromtimestamp(path.getmtime("text_file.txt"))
    print(t2)

    # calculate how long ago the item was modified
    now = datetime.datetime.now()
    td = now - t2
    print("It has been " + str(td) + " since the file was modified")
    print("Or, " + str(td.total_seconds()) + " seconds")


if __name__ == '__main__':
    main()
