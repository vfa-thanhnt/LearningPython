import os
from os import path
import shutil
from shutil import make_archive
from zipfile import ZipFile


def main():
    # make a duplicate of an existing file
    if path.exists("text_file.txt"):
        # get the path to the file in the current directory
        src = path.realpath("text_file.txt")

        # make a backup copy bu appending "bak" to the name
        dst = src + ".bak"

        # copy over the permission, modification times, and other info
        # copy function just copy the content
        shutil.copy(src, dst)
        # copystat function will copy the permission, modification time and other info
        shutil.copystat(src, dst)

        # rename the original file
        # os.rename("text_file.txt", "new_file.txt")

        # put things into a Zip archive
        root_dir, tail = path.split(src)

        # archive all files in root_dir
        shutil.make_archive("archive", "zip", root_dir)

        # more fine-grained control over ZIP files
        with ZipFile("testZip.zip", "w") as newzip:
            newzip.write("text_file.txt")
            newzip.write("text_file.txt.bak")


if __name__ == '__main__':
    main()
