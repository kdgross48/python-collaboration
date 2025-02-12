
classes = ["EECE2140", "EECE2150", "EECE2160", "MATH2321", "MATH2341"]
class_reg =[]

def availableCourses ():
    class_num = 1 
    for i in classes:
        print(str(class_num)+ ". "+i)
        class_num = class_num + 1
        
#=============================================================================
def courseRegistration ():
    course1 = int(input("Please choose a course(enter its number):"))
    class_reg.append(course1)
    course2 = int(input("Please choose a course(enter its number)"))
    class_reg.append(course2)
    course3 = int(input("Please choose a course(enter its number)"))
    class_reg.append(course3)

#=============================================================================
def showRegisteredCourses ():
    class_num = 1 
    for i in class_reg:
        print(str(class_num)+ ". "+i)
        class_num = class_num + 1
    
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
