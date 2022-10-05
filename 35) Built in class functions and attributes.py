# Built in class attributes and functions


def builtin_class_attributes_and_functions():
    class Student:
        def __init__(self):
            self.name = input("Enter your name : ")
            self.age = int(input("Enter your age : "))
            self.gender = input("Enter your gender : ")

        def return_object(self):
            return f"""
Name : {self.name}
Age : {self.age}
Gender : {self.gender} """

    student = Student()
    print(student.return_object())

    print(getattr(student, "gender", "No gender attribute present . The default value is Male"))
    setattr(student, "degree_and_department", "B.E / CSE")
    delattr(student, "gender")
    # print(student.gender)  # It Throws an error
    print(f'"student" object has "degree_and_department" attribute : {hasattr(student, "degree_and_department")}')
    print(f'"student" object has "gender" attribute : {hasattr(student, "gender")}')

    print("'builtin_class_functions' class dictionary : ", Student.__dict__)
    print("'Student' object dictionary : ", student.__dict__)

    print(student.__doc__)
    print(Student.__name__)
    print(student.__module__)
    print(Student.__bases__)


if __name__ == "__main__":
    builtin_class_attributes_and_functions()
