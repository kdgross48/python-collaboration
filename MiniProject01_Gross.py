# -*- coding: utf-8 -*-
"""
Created on Fri Feb  7 13:08:23 2025

"""

classes = ["EECE2140", "EECE2150", "EECE2160", "MATH2321", "MATH2341"]

def availableCourses ():
    index = 1
    for i in classes:
        print(""+str(index)+". "+i)
        index = index + 1
        
#=============================================================================
def courseRegistration ():
    

#=============================================================================
def showRegisteredCourses ():
    print("Skibidi3")
    
#=============================================================================
def systemExit ():
    print("Skibidi4")

#=============================================================================
def main():
    name = (input("Input your name: "))
    decision = int(input("\nWhat would you like to do, " + name + "?\nYou can view available courses (1),\nregister for a course (2),\nview registered courses (3),\nor exit the system (4)?\nYou are limited to a maximum of 3 courses.\n\nDecision: "))
    
    if decision == 1: 
        availableCourses()
    elif decision == 2: 
        courseRegistration()
    elif decision == 3: 
        showRegisteredCourses()
    elif decision == 4: 
        systemExit()
    else:
        decision = input("Invalid number.")
    
#=============================================================================
main()
