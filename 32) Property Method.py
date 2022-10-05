"""
property(fget, fset, fdel, doc) function :-
---------------------------------------------
    Python property() function returns the object of the property class and it is used to create property of a class.
It is a in-built function in python

Syntax :-
-----------
    property(fget, fset, fdel, doc)

Parameters :-
---------------
    (i) fget :- It is used to get the value of the attribute
    (ii) fset :- It is used to set the value of the attribute
    (iii) fdel :- It is used to delete the value of the attribute
    (iv) doc :- It contains the documentation (docstring) for the attibute.

Return Value :-
-----------------
    It returns a property attribute from the given 'getter', 'setter', 'deleter'.

Note :-
--------
    (i) If no arguments are given, property() method returns a base property attribute that doesn't contain any getter, setter or deleter.
    (ii) If doc isn't provided, property() method takes the docstring of the getter function.
"""


def property_method():
    class User:
        def __init__(self, username, password):
            self.__username = username
            self.__password = password

        # Setting the Username and Password
        def set_username(self, username):
            self.__username = username

        def set_password(self, password):
            self.__password = password

        # Returns the Username and Password
        def get_username(self):
            return self.__username

        def get_password(self):
            return self.__password

        username = property(get_username, set_username)
        password = property(get_password, set_password)

    username = input("Enter Username : ")
    password = input("Enter Password : ")

    user = User(username=username, password=password)
    print("Old Username : ", user.username)
    print("Old Password : ", user.password)
    user.username = "Ashwin"
    user.password = "Kannan"
    print("New Username : ", user.username)
    print("New Password : ", user.password)


if __name__ == "__main__":
    property_method()
