"""
5) Hybrid Inheritance :-
---------------------------
    The Hybrid inheritance is a combination of multiple level of inheritance (Generally multiple and multilevel).
The class is derived from the two classes as in multiple inheritance. However, one of the parent class is not the base
class, it is a derived class

    Hybrid inheritance combines more than one form of inheritance. It is a blend of more than one type of inheritance

SYNTAX :-
-----------
                                                ------------
                                                | class A |
                                                ------------
                                                    |
                                                    |
                            ---------------------------------------------------
                            |                                                 |
                            |                                                 |
                        -----------                                       ------------
                        | class B |                                       | class C |
                        -----------                                       -----------
                            |                                                  |
                            |--------------------------------------------------|
                                                    |
                                                    |
                                                -----------
                                                | class D |
                                                -----------
"""


class School:
    def func1(self):
        print("This function is in school")


class Student1(School):
    def func2(self):
        print("This function is in student 1. ")


class Student2(School):
    def func3(self):
        print("This function is in student 2.")


class Student3(Student1, School):
    def func4(self):
        print("This function is in student 3.")


# Driver's code
student = Student3()
student.func1()
student.func2()
