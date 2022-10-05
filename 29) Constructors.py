"""
Constructor :-
-----------------
    A Constructor is a special type of method/function which is used to initialize the instance member/object of the class.

    In C++ or Java, the constructor has the same name of the class, but the python treats the constructor differently.
It is used to create different objects.

    Constructor can be of 2 types. 1) Default Constructor / Non-Parameterized Constructor 2) Parameterized Constructor

    Constructor definition is executed when we create the object of this class. It also verifies that there are enough
resources for the object to performs any start-up tasks

Creating the constructor in python :-
---------------------------------------
    In python, the '__init__()' method simulates the constructor of teh class. This method is called whenever the class is created.
It accepts the 'self' keyword as the first argument which allows the attributes/methods of class.

    We can pass any number of arguments at the time of creating the class object, depending upon the __init__() definition.
It is mostly used to initialize teh class attributes. Every class must have a constructor, if it simply relies on the default constructor.
"""


def constructor():

    """
    Parameterized Constructor :-
    ------------------------------
        The Parameterized Constructor has the multiple parameters along with the 'self' keyword.
    """
    class Student:

        def __init__(self, name, age, roll_no, reg_no, branch, department):
            print("The '__init__()' method/constructor is called everytime when the object/instance is created.")
            self.name = name
            self.age = age
            self.roll_no = roll_no
            self.reg_no = reg_no
            self.branch = branch
            self.department = department

        def print_information(self):
            print("\n------------ Student Information -------------")
            print("Name : ", self.name)
            print("Age : ", self.age)
            print("Roll : No : ", self.roll_no)
            print("Reg : No : ", self.reg_no)
            print("Branch : ", self.branch)
            print("Department : ", self.department)

    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    roll_no = input("Enter your Roll No : ")
    reg_no = int(input("Enter your Reg No : "))
    branch = input("Enter your Branch : ")
    department = input("Enter your department : ")

    student = Student(name=name, age=age, roll_no=roll_no, reg_no=reg_no, branch=branch, department=department)
    student.print_information()

    student2 = Student(name=name, age=age, roll_no=roll_no, reg_no=reg_no, branch=branch, department=department)
    student2.print_information()

    print("Dictionary of 'student' object : ", student.__dict__)
    print("Dictionary of 'student2' object : ", student2.__dict__)
    print("Dictionary of 'Student' class : ", Student.__dict__)

    """ 
    Non-Parameterized Constructor :- 
    -----------------------------------
        The non-parameterized constructor uses when we don't want to manipulate the value (or) the constructor that has only the 'self' as an argument.
    """
    class user:
        def __init__(self):
            print("-------------------------------------")
            print("\nNon - parameterized Constructor")
            self.name = input("Enter your name : ")
            self.age = int(input("Enter your age : "))

        def print_all(self):
            print("Name : ", self.name)
            print("Age : ", self.age)

    user1 = user()
    user1.print_all()

    print("Dictionary of 'user1' object", user1.__dict__)
    print("Dictionary of 'user' class", user.__dict__)

    # Note :- Python doesn't support constructor overloading
    # Constructor Overriding :-
    class ConstructorOverriding:
        def __init__(self):
            print("\nFirst Constructor")

        def __init__(self):
            print("\nSecond Constructor")

    ConstructorOverriding()


if __name__ == "__main__":
    constructor()
