"""
CTEC 121
Matthew Bly
Module 5 Lab 2
code for module 2 lab 5
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""

'''
#practice 1
def main():
    FamilySong("Daddy")
    print()
    FamilySong("Mommy")
    print()
    FamilySong("Brother")
    print()
    FamilySong("Sister")
    print()
    FamilySong("Baby")
    print()


def FamilySong(name):
    print(name, "finger,", name, "finger, where are you?")
    print("Here I am, here I am. How do you do?")
'''


def main2():

#main() 

# practice 2

def Ageclassification(age):
    if age <2:
        return 'I'
    elif age <13:
        return 'C'
    elif age < 18:
        return 'T'
    elif age <= 125:
        return 'A'
    else:
        return 'U'

def testAgeClassification():
    print()
    print(Ageclassification(-1),'expect U: -1 input')
    print(Ageclassification(0), 'expect I: 0 input' )
