# Instance Methods :- Calling a method inside the class, using its object is called instance method.
# Syntax :- <object_name>.<method_name(parameters)>


def instance_method():

    class Student:
        def print_info(self, name, age, roll_no, reg_no, branch, department):
            print("\n------------ Student Details ------------------")
            print("Name : ", name)
            print("Age : ", age)
            print("Roll : No : ", roll_no)
            print("Reg : No : ", reg_no)
            print("Branch : ", branch)
            print("Department : ", department)

    student = Student()
    name = input("Enter your name : ")
    age = int(input("Enter your age : "))
    roll_no = input("Enter your roll no : ")
    reg_no = int(input("Enter your reg no : "))
    branch = input("Enter your branch : ")
    department = input("Enter your department : ")
    student.print_info(name=name, age=age, roll_no=roll_no, reg_no=reg_no, branch=branch, department=department)


if __name__ == "__main__":
    instance_method()
