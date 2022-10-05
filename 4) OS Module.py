# OS Module

import os

print("name function : ", os.name)  # This callback function gives the name of the OS dependent module imported.
print("Current Working Directory ('getcwd() function'): ", os.getcwd()) # It returns a current working directory
print("getcwdb() function : ", os.getcwdb()) # It returns the bytes of the string representing the current working directoy
print('environ function : ', os.environ)# This callback function returns a dictionary of the user's environmental variables
print("getenv() funcion : ", os.getenv('TMP', 'Ashwin')) # It returns the dictionary of user's environmental variables if available, else returns None

os.chdir("F:\\Python programs\\Instagram\\reshma_sathish_\\reshma_sathish_") # It is used to move from one directory to another directory by giving it's path.
print("After Changing the directory ('chdir() function') : ", os.getcwd())

os.mkdir("F:\\Python programs\\Tutor Joes Stanley\\Test Folder") # It creates a new directory at the specified path if they don't already exists.
os.rmdir("F:\\Python programs\\Tutor Joes Stanley\\Test Folder") # It removes a specified directory at the specified path if they already exists.

os.makedirs("F:\\Users\\mike\\Documents\\pytest\\2014\\02\\19") # It will create all the intermediate folders in a path recursively if they don't already exists.
os.removedirs("F:\\Users\\mike\\Documents\\pytest\\2014\\02\\19") # It will remove all the intermediate folders in a path recursively if they already exists.

#os.remove("C:\\Users\\ASHWINKANNAN\\New folder\\Simple Text.txt") # It will remove the file if they already exists in the specified path.

print("listdir(path=None) function : ", os.listdir()) # It will list all the files and folders at the specified folder (or) at the default folder

print("system(command) function :- ", os.system('notepad')) # It will execute a shell command (string) in a sub-process. Returns the error code as integer. Whenever this method is used, then the respective shell of the OS is opened and the command is executed on it.

print('getpid() function :- ', os.getpid()) # Returns the process ID of the current process.
print("Parent Process ID of current process is ('getppid()' function) :- ", os.getppid()) # Returns the parent's process ID of the child process.

print('terminal_size() function :- ', os.terminal_size((80, 24))) # It is used to set the size of the terminal window

#os.rename("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Additional information\\Waste.pdf",
#          'C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Additional information\\waste.pdf')  # It is used to rename a file (or) folder

#os.renames("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Additional information\\waste.pdf",  # It is a recursive directory (or) file renaming function. 
#           "C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Waste information\\Waste.pdf") # It works like 'os.rename()' method except creation of any intermeiate directories needed , then it is attempted first

#os.replace("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Waste information\\Waste.pdf", # It is used to rename the file (or) directory.
#           "C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Waste information\\waste.pdf")

os.popen('C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Waste information\\waste.pdf', 'r') # It is used to opens a pipe to (or) from command. The return value is an open file object connected to the pipe, which can be read/written.

print('getlogin() function :- ', os.getlogin()) # It is used to get the name of the user logged in on the controlling terminal of the process.

print("abc : ", os.abc)
print("times() function :- ", os.times()) # It returns the current global process times

print('cpu_count() function :- ', os.cpu_count()) # It is used to get the number of CPU's in the system. It returns None if the number of CPU's in the system is undetermined.

#print('uname_result() function :- ', os.uname_result()) # 

print('get_exec_path(env=None) function :- ', os.get_exec_path()) # It returns the list of folders that will be searched for a named executable while launching a process

#os.truncate("C:\\Users\\ASHWINKANNAN\\OneDrive\\Desktop\\Waste information\\waste.pdf", 500) # It truncates the file corresponding to path, so that it is at most length bytes in size. This function can support file descriptor too.

print("device_encoding(fd) function :- ", os.device_encoding(500)) # It is used to get the encoding of the device associated with the specified file descriptor, if it is connected to the terminal. It returns None, if the specified file descriptor is not connected to a terminal.

read, write = os.pipe() # It is used to create a pipe. A pipe is a function to pass information from one process to another process. It offers only one-way communication and the passed information is held by the system until it is read by the receiving process. It returns a pair of file descriptors (r, w) usable for reading and writing respectively.
print("pipe() function :- ", (read, write))

print("Connected to a terminal ('isatty(fd)'):- ", os.isatty(write)) # It is used to check whether the file descriptor is open and connected to a tty device or not.

print('stat() function :- ', os.stat('F:\\Python programs\\Tutor Joes Stanley\\5) OS_Path module.py'))

print('os.curdir() function :- ', os.curdir)

os.kill(os.getpid(), 2) # os.kill() function # It is used to specific signal to the process with the specified process ID. Constant for the specific signal availableon the host platform are defined in the signal module.

print('abort() function :- ', os.abort()) # Aborts the interpreter immediately. The code after 'abort()' function will not be executed by the interpreter.
print("This statement will not be printed")



