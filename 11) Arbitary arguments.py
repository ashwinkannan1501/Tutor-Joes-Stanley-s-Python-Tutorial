# Arbitary Arguments :-

def print_names(*names):
    print(names)


candidate, father, mother = input("Enter Candidate name, Father name and Mother name respectively (Separated By Comma) :- ").split(",")
print_names(candidate, father, mother)
