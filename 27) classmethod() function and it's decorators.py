"""
classmethod() function and it's decorators in python:-
---------------------------------------------------------
    The classmethod() is an in-built function in Python, which returns a class method for a given function.
classmethod() methods are bound to a class rather than an object. Class methods can be called by both class and object.
These methods can be called with a class or with an object.

Syntax:-
---------
    classmethod(function)

Parameter :-
--------------
    This function accepts the function name as a parameter.

Return Type:-
---------------
    This function returns the converted class method.

The @classmethod Decorator :-
-------------------------------
    The @classmethod decorator is a built-in function decorator which is an expression that gets evaluated after your
function is defined. The result of that evaluation shadows your function definition.

    A class method receives the class as the implicit first argument, just like an instance method receives the instance.

Syntax:
---------
class C(object):
    @classmethod
    def fun(cls, arg1, arg2, ...):
       ....
Where,
    fun:- the function that needs to be converted into a class method
    returns:- a class method for function.

Note:-
--------
    A class method is a method which is bound to the class and not the object of the class.
    They have the access to the state of the class as it takes a class parameter that points to the class and not the object instance.
    It can modify a class state that would apply across all the instances of the class. For example, it can modify a class variable that would be applicable to all the instances.
"""


def classmethod_function():
    class Student:
        total_students = 0

        def __init__(self, name, age, gender):
            self.name = name
            self.age = age
            self.gender = gender
            Student.total_students += 1

        def print_details(self):
            print("Name : ", self.name)
            print("Age : ", self.age)
            print("Gender : ", self.gender)

        @classmethod
        def class_strength(cls):
            return cls.total_students

    print("Total students : ", Student.class_strength())
    student1 = Student("K.Ashwin", 21, "Male")
    student1.print_details()
    print("Total students : ", student1.class_strength())

    student2 = Student("S.Reshma", 21, "Female")
    student2.print_details()
    print("Total students : ", student2.class_strength())

    student3 = Student("S.Kowshik", 21, "Male")
    student3.print_details()
    print("Total students : ", student3.class_strength())

    print("Total students : ", student1.class_strength())


if __name__ == "__main__":
    classmethod_function()
