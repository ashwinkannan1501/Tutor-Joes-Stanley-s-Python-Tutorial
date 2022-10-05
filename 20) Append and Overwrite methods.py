# Append and Overwrite method using 'a' mode and write() method.

# Append method
try:
    fileObject = open(file="Append concept in python.txt", mode='a+')

    fileObject.write("\nI am a powerful programmer")
except Exception as e:
    print(e)
else:
    fileObject = open(file="Append concept in python.txt", mode='r')
    print(fileObject.read())
finally:
    fileObject.close()

# OverWrite Method
file = open(file="Overwrite Concept in Python", mode="w+")
file.write("I am a powerful mobile and web app developer")
print(file.read())
file.close()
