# Input Multiple lines

print("Enter a paragragh : ")

array = []

while True:
    line = input()
    if line:
        array.append(line)
    else:
        break

print(' '.join(array))


        
    
