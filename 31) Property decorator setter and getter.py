#

"""
Property Decorator Setter and Getter :-
-----------------------------------------
    Python @property is one of the built-in decorators. @property decorator in Python which is helpful in defining the
properties effortlessly without manually calling the inbuilt function property(). The @property decorator is for
creating getters and setters.

    The getters and setters are not the same as those in other object-oriented programming languages. Basically, the
main purpose of using getters and setters in object-oriented programs is to ensure data encapsulation. Private variables
in python are not actually hidden fields like in other object-oriented languages.
"""


def property_decorator_setter_and_getter():
    class UserProfile:

        def __init__(self, username, password):
            self.__username = username  # Private username
            self.__password = password  # Private Password

        # Property Getters (Getting the username and password)
        @property
        def get_username(self):
            return self.__username

        @property
        def get_password(self):
            return self.__password

        # Property Setters (Setting the username and password)
        @get_username.setter
        def set_username(self, username):
            self.__username = username

        @get_password.setter
        def set_password(self, password):
            self.__password = password

    username = input("Enter your username : ")
    password = input("Enter your password : ")

    user1 = UserProfile(username=username, password=password)
    print("Old Username : ", user1.get_username)
    print("Old Password : ", user1.get_password)
    user1.username = "Ashwin"
    user1.password = "Kannan"
    print("New Username : ", user1.username)
    print("New Password : ", user1.password)


if __name__ == "__main__":
    property_decorator_setter_and_getter()
