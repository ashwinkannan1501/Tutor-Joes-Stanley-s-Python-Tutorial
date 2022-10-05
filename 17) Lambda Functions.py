# Lambda Functions

first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))

add = lambda a, b: first_number + second_number
sub = lambda a, b: first_number - second_number
multiply = lambda a, b: first_number * second_number
division = lambda a, b: first_number / second_number

print(f"""
{first_number} + {second_number} = {add(first_number, second_number)}
{first_number} - {second_number} = {sub(first_number, second_number)}
{first_number} * {second_number} = {multiply(first_number, second_number)}
{first_number} / {second_number} = {division(first_number, second_number)}
""")
