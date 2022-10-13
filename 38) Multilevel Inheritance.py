"""
2) MULTILEVEL INHERITANCE :-
-------------------------------
    In Multilevel Inheritance, features of the base class and the derived class are further inherited into the new
derived class. This is similar to a relationship representing a child, father and a grandfather.

SYNTAX :-
----------
    -----------
    | class A | (Base (or) Parent (or) Super Class) (Base Class)
    -----------
        |
        |
    ------------
    | class B | (derived class of class A) (Intermediate Class)
    -----------
        |
        |
    -----------
    | class C | (derived class of class B) (Derived Class)
    -----------
"""


class GrandFather:
    def property(self):
        print("GrandFather has it's property. Grandson has access to his property")


class Father(GrandFather):
    def bike(self):
        print("Father Owns a bike. Son can access his father's bike")


class Son(Father):
    def bicycle(self):
        print("Son owns his bicycle")


son = Son()
son.property()
son.bike()
son.bicycle()
