"""
super() function :-
----------------------
    The super() function is used to give access to the methods and attributes of a parent class. It returns a temporary
object of a parent class when used.

SYNTAX :-
-----------
    super() -> No Parameter/Argument Values
"""
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Square(Rectangle):
    def __init__(self, length, width):
        super().__init__(width=width, length=length)


class Cube(Rectangle):
    def __init__(self, length, width, height):
        super().__init__(width=width, length=length)
        self.height = height

    def volume(self):
        return self.length * self.width * self.height


length = int(input("Enter the length value : "))
width = int(input("Enter the width value : "))
height = int(input("Enter the height value : "))

rectangle = Rectangle(width=width, length=length)
square = Square(length=length, width=width)
cube = Cube(height=height, width=width, length=length)

print(f"The are of a rectangle of length {length} and width {width} is : {rectangle.area()}")
print(f"The are of a square of length {length} and width {width} is : {square.area()}")
print(f"The Volume of cuboid of length {length}, width {width} and height {height} is : {cube.volume()}")
