from multipledispatch import dispatch


class MethodOverloading:
    @dispatch(int, int)
    def add(self, first_number, second_number):
        print(f'{first_number} + {second_number} = {first_number + second_number}')

    @dispatch(int, int, int)
    def add(self, first_number, second_number, third_number):
        print(f'{first_number} + {second_number} + {third_number} = {first_number + second_number + third_number}')


first_number = int(input("Enter the first number : "))
second_number = int(input("Enter the second number : "))
third_number = int(input("Enter the third number : "))

method_overloading = MethodOverloading()
method_overloading.add(first_number, second_number)
method_overloading.add(first_number, second_number, third_number)
