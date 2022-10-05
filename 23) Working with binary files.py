# Binary files :-

import pickle
import os


def write_into_binary_file(lists, filename):
    try:
        file = open(mode="ab", file=filename)
    except Exception as error:
        print(error)
    else:
        pickle.dump(obj=lists, file=file)
        print(f"The list '{lists}' is written successfully into '{os.path.abspath(filename)}'")
    finally:
        file.close()
        print("The Program is terminated successfully")


def read_from_binary_file(filename, lists):
    try:
        fileobject = open(mode="rb", file=filename)
    except Exception as error:
        print(error)
    else:
        print(pickle.load(file=fileobject))
        print(f"The list '{lists}' is read from the file '{os.path.abspath(filename)}' successfully")
    finally:
        fileobject.close()
        print("The program was terminated successfully")


array = list(input("Enter the list elements :- ").split(","))

file_name = "binary_file.txt"

write_into_binary_file(filename=file_name, lists=array)
read_from_binary_file(filename=file_name, lists=array)



