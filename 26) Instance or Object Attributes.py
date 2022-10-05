"""
Instance (or) Object Attributes :-
-----------------------------------
    When the objects get created to form the class, they no longer depend on the class attribute.
Also, the class has no control over the attributes of the instances created.

    If the attributes are available in objects, returns and prints the attributes in respective class and returns the
value.
"""


def instance_attribute():
    class user_profile:
        course = "Java"

    print("Class Dictionary : ", user_profile.__dict__)
    user1 = user_profile()  # Creates the 'user1' object
    print("Dictionary of 'user1' object : ", user1.__dict__)
    # Prints Class Attributes because 'user1' object has no value in it. When the object has no value, it returns it's class value. When the object has it's value, it retuns it's own value itself
    print("Prints the Class Attribute : ", user1.course)
    user1.course = "C++"  # Changes the 'user1' object value to 'C++'
    print(user1.__dict__)  # 'user1' object namespace
    print(user1.course)  # Prints Object Attributes
    user2 = user_profile()
    user2.course = "Python"
    print(user2.__dict__)
    print(user2.course)  # Prints 'user2' Object Attributes


if __name__ == "__main__":
    instance_attribute()
