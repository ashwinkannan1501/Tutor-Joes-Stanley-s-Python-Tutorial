# Passing list as arguments and parameters

def list_as_arguments(lists):
    print("List Elements : ", lists)

list_elements = input("Enter the list values separated by comma (,) :- ").split(",")
list_as_arguments(lists=list_elements)
