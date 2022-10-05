# Open a file

try:
    file = open(mode="r", file="random text.txt")

    # for line in file:
    #     print(line)
except FileNotFoundError:
    file = open(mode="a", file="random text.txt")
    file.write("\nHello I am K. Ashwin")
    file.close()

else:
    print(file.readline())
    print(file.readline())
    print(file.readline(15))
    print(file.readlines())
    print(file.read())


finally:
    file.close()


# -----------------------------------------------------------


