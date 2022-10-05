# Delete a file and a folder
import os
import shutil
import send2trash

# Delete a file
try:
    fileobject = open(mode="xt", file="file.txt")
    os.remove("file.txt")
    # if os.path.isfile("file.txt"):
    #     os.remove("file.txt")
    # else:
    #     print("That is not a file . that is a folder")

except FileExistsError:
    print(f'The file {os.path.basename("file.txt")} is already present in the {os.path.abspath("file.txt")}')
# except FileNotFoundError:
#     print(f'The file "{os.path.abspath("file.txt")[-8:]}" is not found in the "{os.path.abspath("file.txt")}" (or) already deleted')
except PermissionError as permission_error:
    print(permission_error)
else:
    print(f"The empty folder named {os.path.basename('file.txt')} is created in the {os.path.abspath('folder')} and deleted successfully")
finally:
    print("The Program is terminated without any error")

print("------------------------------------------------------------------------------------------------------------")

# Delete a empty folder
try:
    os.mkdir("folder")
except IsADirectoryError as e:
    print(e)
except FileExistsError:
    print(f"The file/folder named {os.path.basename('folder')} already exists in the {os.path.abspath('folder')}")
else:
    os.rmdir("folder")
    print(f"The empty folder named {os.path.basename('folder')} is created in the {os.path.abspath('folder')} and deleted successfully")
finally:
    print("The Program was terminated successfully without any error")

print("------------------------------------------------------------------------------------------------------------")

# Delete a folder with a file
folder_name = "folder"
file_name = "file2.txt"
try:
    os.mkdir(folder_name)
    os.chdir(folder_name)
    filename = open(mode="xt", file=file_name)
    os.chdir("../folder")
    send2trash.send2trash("F:\\Python programs\\Tutor Joes Stanley\\folder")

    #send2trash.send2trash('F:\\Python programs\\Tutor Joes Stanley\\folder\\')
    # os.unlink('folder\\file2.txt')

except FileExistsError:
    print(f'The file/folder named {os.path.basename(file_name)} (or) {os.path.basename(folder_name)} is already exists')
except FileNotFoundError:
    print(f'The file/folder named {os.path.basename(file_name)} (or) {os.path.basename(folder_name)} is not exists')
except OSError as osError:
    print(osError)
finally:
    print("The Program was terminated successfully")



