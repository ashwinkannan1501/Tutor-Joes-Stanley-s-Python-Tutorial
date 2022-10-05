# Read a file using readline() and readlines() method

try:
    file_object = open(mode="r", file="random text.txt")
except FileNotFoundError:
    print(f"The file {file_object} is not found in the directory. Don't worry we created it for you in the project directory")

    file_object = open(mode="a+", file="random text.txt")
    file_object.close()
else:
    print(file_object.readline())
    print(file_object.readline(8))
    print(file_object.readlines(8))
    print(file_object.readlines())
finally:
    file_object.close()

