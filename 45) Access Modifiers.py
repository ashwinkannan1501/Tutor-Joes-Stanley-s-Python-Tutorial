"""
Access Modifiers :-
---------------------
    The Access Modifiers are used to control the access levels. There are 3 types of access modifiers. They are :-
        (i) Public Access Modifier
        (ii) Private Access Modifier
        (iii) Protected Access Modifier

    (i) Public Access Modifier :-
    -------------------------------
        The class and the code is accessible by any other class is called "public access modifier"

    (ii) Private Access Modifier :-
    ----------------------------------
        The code is accessible only within the declared class is called  "private access modifier"

    (iii) Protected Access Modifier :-
    --------------------------------------
        The code is only accessible in the same package and the subclasses is called "protected access modifier"

    NOTE :-
    --------
        (i) For Classes, you can use pubic access modifier
        (ii) For attributes, methods and constructors, you can either use the public, private or protected access modifiers
"""


class AccessModifiers:
    name = input("Enter your name : ")  # Public access modifier
    _age = int(input("Enter your age : "))  # protected access modifier. It is denoted as '_'variable_name.
    __gender = input("Enter Your Gender (M/F) : ")  # private access modifier. It is denoted as '__'variable_name
    __gender.removesuffix(__gender[0]).upper()

    def __display(self):  # private method
        print("Name : ", self.name)
        print("Age : ", self._age)
        print("Gender : ", self.__gender)


access_modifiers = AccessModifiers()
print("Name : ", access_modifiers.name)
print("Age : ", access_modifiers._age)
print("Gender : ", access_modifiers.__gender)  # It will throw an error
access_modifiers.__display()  # It will throw an error
