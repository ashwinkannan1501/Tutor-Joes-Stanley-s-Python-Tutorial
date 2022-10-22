"""
Method Overriding :-
-----------------------
    We can provide some specific implementation of teh parent class method in out child class. When the parent class
method is defined in the child class with some specific implementation, then the concept is called 'method overriding'.
We may need to perform method overriding in teh scenario where the different definition of the parent class method is
needed in the child class.

    Two methods with same name and the same parameters is known as method signature.

                                        (or) (another definition)

    Method overriding in Python is when you have two methods with the same name that each perform different tasks.
Method overriding is an ability of any object-oriented programming language that allows a subclass or child class to
provide a specific implementation of a method that is already provided by one of its super-classes or parent classes.
When a method in a subclass has the same name, same parameters or signature and same return type(or sub-type) as a
method in its super-class, then the method in the subclass is said to override the method in the super-class.
"""


class Employee:
    def WorkingHrs(self):
        self.hrs = 6

    def printHrs(self):
        print(f"The Employee must work at-least {self.hrs} per day")


class Trainee(Employee):
    def WorkingHrs(self):
        self.hrs = 8

    def printHrs(self):
        print(f"The Trainee must work at-least {self.hrs} per day")

    # def resetHrs(self):
    #     super().WorkingHrs()


employee = Employee()
employee.WorkingHrs()
employee.printHrs()

trainee = Trainee()
trainee.WorkingHrs()
trainee.printHrs()
# Reset Trainee Hrs
# trainee.resetHrs()
# trainee.printHrs()