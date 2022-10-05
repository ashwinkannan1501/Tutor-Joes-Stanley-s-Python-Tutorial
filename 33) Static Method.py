def staticmethod_function():
    class User:
        def __init__(self):
            self.name = input("Enter your name : ")
            self.age = int(input("Enter your age : "))
            self.gender = input("Enter your gender : ")

        def print(self):
            print("Name : ", self.name)
            print("Age : ", self.age)
            print("Gender : ", self.gender)

        @staticmethod
        def welcome():
            print("Welcome to Panimalar Engineering College \n")

    user1 = User()
    user1.print()
    user1.welcome()

    user2 = User()
    user2.print()
    user2.welcome()

    User.welcome()


if __name__ == "__main__":
    staticmethod_function()
