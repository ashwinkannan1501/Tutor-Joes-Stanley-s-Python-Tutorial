# Arbitary Keyword Arguments

def details(**values):
    return values


try:
    name = input("Enter Your Name :- ")
    age = int(input("Enter your Age :- "))
    gender = input("Enter your Gender :- ").lower()
except NameError:
    print("Please provide the correct value")
except ValueError:
    print("Please provide the Correct value")
else:
    while True:
        if gender == "male" or gender == 'female':
            print(details(gender=gender, age=age, name=name))
            break
        else:
            print("Please enter either 'Male' or 'Female'. No other words can be accepted")
            gender = input("Enter your Gender :- ").lower()
