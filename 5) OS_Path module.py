
# os.path module
import os

path1 = 'F:\\Android development\\MyFirstApplication\\app\\src\\main\\java\\com\\example\\myfirstapplication\\Program_12_Scroll_View.java'
path2 = 'F:\\Python programs\\Tutor Joes Stanley\\5) OS_Path module.py'

print('basename(path) function :- ', os.path.basename("F:\\Android development")) # It is used to return the basename of the file (or) directory

print('dirname(path) function :- ', os.path.dirname(path2)) # It is used to return the directory name from the given path. This function returns the name from the path except the pathname.

print('isabs(path) function :- ', os.path.isabs("F:\\Android development")) # It returns True/False based on whether the path is absolute (or) not.
print('isdir(path) function :- ', os.path.isdir("F:\\Python programs")) # It returns True/False based on whether the given path is a existing directory (or) not.
print('isfile(path) function :- ', os.path.isfile(path2)) # It returns True/False based on whether the given path is a existing file (or) not.

print('sys() function :- ', os.path.sys) # This function gives the system of the OS module.

print('abspath(path) function :- ', os.path.abspath(path1)) # It returns the normalized absoluted version of the pathname path. It returns the pathname of the path passed as a parameter to this function. It prints the absolute path of the current workinfg directory with filename.


paths = ['F:\\Python programs\\Tutor Joes Stanley\\5) OS_Path module.py',
         'F:\\Python programs\\Tutor Joes Stanley\\4) OS Module.py']
print('commonpath(list) function :- ', os.path.commonpath(paths)) # It is used to get the longest common sub-path in a list of paths. It raises 'ValueError' if the specified list of paths either contains both absolute and relative path, or is empty, or if the both drives are different (Windows OS). The returned path is a string of valid path. 
print('commonprefix() function :- ', os.path.commonprefix(paths)) # It is used to get the longest common path prefix in a list of paths. It returned only common prefix value in the specified list, returned may (or) may not be a valid pathas it checks for a common prefix by comparing character by character in the list.


print('normpath(path) function :- ', os.path.normpath('F:/aschac/./sdvkjsdv//DVSADVI/SDVSDV')) # It is used to normalize the specified path. All redundant separator and up-level references are collapsed in the process of path normalization. On Windows OS, any '/' is converted into '\'.
print('normcase(path) function :- ', os.path.normcase('F:/aschac/./sdvkjsdv//DVSADVI/SDVSDV')) # It is used to normalize the case (upper and lower case) of the specified pathname. On windows, it converts all the charcters in the specifiedf path to the lowercase and '/' to '\'. It returns the specified path unchanged omn OS other than windows

print('getsize(path) function :- ', os.path.getsize(path2)) # It returns the size of the specifed path in bytes(int). It raises OSError if the file doesn't exists (or) if somehow inacessible.

#print('os() function :- ', os.path.os())

print('realpath(path) function :- ', os.path.realpath("F:\\Python programs\....\Tutor Joes Stanley\\4) OS Module.py")) # It returns the canonical path of the specified filename by eliminating any symbolic links encountered in the path.

print('getatime(filename) function :- ', os.path.getatime(path1)) # It is used to get the time of the last access of the specified path.
print('getctime(filename) function :- ', os.path.getctime(path1)) # It is used to get the system's c-time of the specified path. Here, 'c-time' refers to the last metadata change for specified path in UNIX while in windows, it refers to the path creation time.
print('getmtime(filename) function :- ', os.path.getmtime(path1)) # It is used to get the time of the last modification of the specified path.

print('samefile(path1, path2) function :- ', os.path.samefile(path1, path1)) # It is used to check whether the given two pathnames refers to the same file (or) directory (or) not.

print('exists(path) method :- ', os.path.exists(path2)) # It returns a boolean value based on whether the specified path is exists (or) not. It is also used to check whether the given path refers to an open file descriptor (or) not.
print('lexists() function :- ', os.path.lexists('F:\\Python programs\\Tutor Joes Stanley\\4) OS Module.py')) # It returns a bollean value based on whether the given path is exists (or) not. Unlike 'os.path.exists()' function, it returns True for broken symbolic link. It behaves similar to 'os.path.exists()' on the platform where 'os.path.lstat()' function is not available.

print('ismount() function :- ', os.path.ismount('E:')) # It returns a boolean value based on whether the given path is mount point (or) not. A mount point in a file system where different file systems have been mounted.

print('join(path, *paths) function :- ', os.path.join("E:\\",'Ashwin\\', 'Kannan\\', 'Amutha\\')) # It is used to join one (or) more path components intelligently. It concates various path components with exactly one folder separator.

print('split(path)function :- ', os.path.split("F:\\Python programs\\Tutor Joes Stanley\\4) OS Module.py")) # It is used to split the pathname into a pair of head and tail. here, tail is the last pathname component and head is everything leading upto that.
print('splitext(path) function :- ', os.path.splitext("/home/user/file.txt")) # It is used to split the pathnames into a pair of root and extension.
print('splitdrive() function :- ', os.path.splitdrive(path2)) # It is used to split the pathname into a pair of drive and tail.

print("support_unicode_filenames :- ", os.path.supports_unicode_filenames) # It returns a boolean value based on whether an arbitary unicode strings can be used as filenames (or) not.
