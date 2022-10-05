"""
Class Methods :-
-------------------
    The Methods are declared within class, and they are used to perform certain task. The methods
are actually functions. In general, the functions are called methods in OOP. To call the class
methods, syntax is "<class_name>.<method_name()>"

    A Class method is a method that's shared among all objects. To call a class method, put the class as first argument
"""


def class_methods():
    class Student:
        name = "K.Ashwin"
        age = 21
        roll_no = "2019PECCS365"
        reg_no = 211419104026
        branch = "Bachelor Of Engineering"
        department = "Computer Science and Engineering"

        @staticmethod
        def print():
            print("Name : ", Student.name)
            print("Age : ", Student.age)
            print("Roll : No : ", Student.roll_no)
            print("Reg : No : ", Student.reg_no)
            print("Branch : ", Student.branch)
            print("Department : ", Student.department)

    Student.print()
    print(Student.__dict__)

    print("--------------------------------------------------------")
    print(getattr(Student, "print"))
    getattr(Student, "print")()
    Student.__dict__['print']()


if __name__ == "__main__":
    class_methods()
