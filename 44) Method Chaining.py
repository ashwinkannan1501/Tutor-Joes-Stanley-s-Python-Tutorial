"""
Method Chaining :-
---------------------
    The Method Chaining is the process of calling different methods in a single line instead of calling other methods
with the same object reference separately.

    Under this procedure, we have to write the object reference once and then call the methods by separating them with
a dot notation (.)

    It is also known as parameter idioms (or) train wreck because of ṭhe increase in the number of methods even though
line breaks are often added between methods.

SYNTAX :-
----------
    ----------------------------------------
    | obj.method1().method2().method3()... |
    ----------------------------------------

    Invoking methods one after the another is called method chaining.

"""
class Car:
    def start(self):
        print("You started the car engine")
        return self

    def drive(self):
        print("You are currently driving the car")
        return self

    def brake(self):
        print("You stepped on the brake")
        return self

    def stop(self):
        print("You stopped the car and turn off the engine")
        return self


car = Car()
car.start().drive().brake().stop()
