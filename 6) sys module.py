# sys module
import sys

print("version :- ", sys.version)
print()

print("hexversion :- ", sys.hexversion)
print()

print('hex(hexversion) :- ', hex(sys.hexversion))
print()

print("version_info :- ", sys.version_info)
print()

print("winver :- ", sys.winver)
print()

print("stdin :- ")
for line in sys.stdin:
    if(line.rstrip() == 'q'):
        break
print("Exit")

sys.stdout.write("This is 'sys.stdout' variable \n")
print()

sys.stderr.write("This is 'sys.stderr' error message \n")
print()

print("path :- ", sys.path)
print()

print('modules :- ', sys.modules.keys())
print()

print("api_version :- ", sys.api_version)
print()

print("platform :- ", sys.platform)
print()

print('getwindowsversion :- ', sys.getwindowsversion())
print()

print('getrefcount(object) function :- ', sys.getrefcount("Ashwin"))
print()

#print('setprofile() :- ', sys.setprofile(sys.hexversion))

print('maxsize :- ', sys.maxsize)
print()

print('thread_info :- ', sys.thread_info)
print()

print('getdefaultencoding() function :- ', sys.getdefaultencoding())
print()

print('getsizeof(object, default=None) function :- "Hello" has ', sys.getsizeof('hello', 0) , "bytes of memory ")
print()

print('flags :- ', sys.flags)
print()

print('builtin_module_names :- ', sys.builtin_module_names)
print()

print('exec_info :- ', sys.exc_info())
print()

print('executable :- ', sys.executable)
print()

print("byteorder :- ", sys.byteorder)
print()

print('argv : ', sys.argv)
print()

print("getfilesystemencoding() function :- ", sys.getfilesystemencoding())
print()

print("getcheckinterval() function :- ", sys.getcheckinterval())
print()

print('getswitchinterval() function :- ', sys.getswitchinterval())
print()

print('hash_info :- ', sys.hash_info)
print()

print('callstats() function :- ', sys.callstats())
print()

print('getfilesystemencodeerrors() function :- ', sys.getfilesystemencodeerrors())
print()

print('gettrace() function :- ', sys.gettrace())
print()

print('exit() function :- ', sys.exit("Hello"))



