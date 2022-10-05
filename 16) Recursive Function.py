# Recursive Function :- A function calls by itself again and again is called recursive function

# Factorial of a given number

#3 * 2 * 1
def factorial(num):
    if num == 1:
        return f'The factorial of {num} is {num}'
    else:

        return (num * factorial(num - 1))


number = int(input("Enter a number : "))

print(f'The Factorial of {number} is :- {factorial(num=number)}')
