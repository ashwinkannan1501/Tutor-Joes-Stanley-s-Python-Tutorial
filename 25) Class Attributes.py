"""
Class Attributes :-
---------------------
    the attributes are actually variables. In general the variables are called as the attributes in OOP.
"""


def class_attributes():
    class Student:
        name = "K. Ashwin"
        age = 21
        roll_no = "2019PECCS365"
        reg_no = 211419104026

    # We can get the attribute value using the 'getattr()' method
    print("Name : ", getattr(Student, "name", "No such attribute found"))
    print("Gender : ", getattr(Student, "gender", "No such attribute found in the class. The default value is 'Male'"))

    # We can get the attribute value using dot notation
    print("Age : ", Student.age)
    print("Roll No : ", Student.roll_no)
    print("Reg No : ", Student.reg_no)

    # We can set the attribute value using 'setattr()' method
    setattr(Student, "gender", "Male")
    print("Gender : ", Student.gender)

    # We can set the attribute value using dot notation
    Student.city = "Chennai"
    print("City : ", Student.city)

    print("__dict__ : ", Student.__dict__)
    # We can delete a attribute using 'delattr()' method
    delattr(Student, "gender")
    print("After deleting 'gender' attribute : ", Student.__dict__)

    # We can delete a attribute using 'del' keyword
    del Student.city
    print("After deleting 'city' attribute : ", Student.__dict__)


if __name__ == "__main__":
    class_attributes()
