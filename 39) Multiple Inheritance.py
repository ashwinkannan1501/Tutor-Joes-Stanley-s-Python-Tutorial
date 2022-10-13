"""
3) MULTIPLE INHERITANCE :-
--------------------------------
    When a class can be derived from more than one base class, this type of inheritance is called multiple inheritance.
In multiple inheritance, all the features of the base classes are inherited into the single derived class.

SYNTAX :-
-----------
    -----------              ------------
    | class A |              | class B |
    -----------              -----------
        |                         |
        --------------------------
                    |
                -----------
                | class C |
                -----------
"""


class Father:
    def business(self):
        print("Father can do his own business. He is self employed.")


class Mother:
    def cook(self):
        print("Mother is a house-wife. She do excellent cooking")


class Son(Father, Mother):
    def read(self):
        print("Son did excellent Performance in reading")


son = Son()
son.business()
son.cook()
son.read()

