"""
Python property decorator - @property :-
------------------------------------------
    A decorator feature in python wraps in a function, appends several functionality to existing code and then returns it.
Methods/functions are known to be callable as they can be called. Therefore, a decorator is also callable and returns callable.
This is also known as 'meta-programming' as at compile time of section of program alters another section of program
"""


def property_decorator():
    class PropertyDecorator:
        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
            #self.print = f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}"

        """
        @property decorator :- 
        -------------------------
            '@property' decorator is a built-in decorator in python which is helpful in defining the properties 
effortlessly without manually calling the in-built 'property()' function.
            It returns the property attribute of a class from the stated 'getter', 'setter', 'deleter' as parameter.
        """
        @property
        def information(self):
            return f"Name : {self.name}\nAge : {self.age}\nGender : {self.gender}"

    property_decorator = PropertyDecorator("K.Ashwin", 21, "Male")

    print("-------------Old Information---------- \n", property_decorator.information)
    property_decorator.age = 45
    print("\nNew Age : ", property_decorator.age, "\n")
    print("-------------New Information---------- \n", property_decorator.information)


if __name__ == "__main__":
    property_decorator()
