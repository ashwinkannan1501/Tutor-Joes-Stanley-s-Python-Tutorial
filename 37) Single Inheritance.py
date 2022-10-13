"""
Inheritance :-
----------------
    The Inheritance is an important aspects of the object-oriented paradigm. The Inheritance provides the code
re-usability to the program because we can use an existing class to create a new class instead of creating it from
scratch.

    In Inheritance, the child class acquires the properties and can access all the data members and functions defined in
the parent class. A child class can also provide it's specific implementation to the functions of the parent class.

    In python, a derived class can inherit the base class by just mentioning base class in the bracket after the derived
class name.

    In Python, a derived class can inherit attributes and methods from one class to another class. We group the
inheritance concept into 2 categories. They are :-

1) Base Class (parent (or) Superclass) :-  The class that being inherited from
2) Derived Class (Child (or) Subclass) :- The class that inherits from another class

Different Types of Inheritance in Python :-
----------------------------------------------
    1) Single Inheritance
    2) Multilevel Inheritance
    3) Multiple Inheritance
    4) Hierarchical Inheritance
    5) Hybrid Inheritance

1) SINGLE INHERITANCE :-
--------------------------
    The single inheritance enables the derived class (or) child class (r) subclass to inherit the properties from a
single base class (or) parent class (or) superclass, thus enabling the code re-usability and the addition of new features
to the existing code

SYNTAX :-
-----------
    -----------
    | class A | (Parent (or) base (or) Super Class)
    -----------
        |
        |
     ----------
    | class B | (Derived (or) Child (or) Sub-Class)
    -----------
"""


class Apple:
    def __init__(self):
        self.company_name = "Apple-India"
        self.company_website = "https://www.apple.com/in/"
        self.contact_details = "000800 040 1966"


class Iphone14Pro(Apple):
    def phone_details(self):
        self.phone_brand = "Apple"
        self.phone_name = "iphone 14 Pro"
        self.phone_storage = "1TB"
        self.phone_ram = "6GB"
        self.default_os = "ios16"
        self.launch_year = 2022


mobile = Iphone14Pro()
print("Company Name : ", mobile.company_name)
print("Company Website : ", mobile.company_website)
print("Company Contact Details : ", mobile.contact_details)
mobile.phone_details()
print("Phone Brand : ", mobile.phone_brand)
print("Phone Name : ", mobile.phone_name)
print("Phone Storage : ", mobile.phone_storage)
print("Phone RAM : ", mobile.phone_ram)
print("Default OS : ", mobile.default_os)
print("Phone Launch Year : ", mobile.launch_year)


