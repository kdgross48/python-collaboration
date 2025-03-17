import cmath

class Firstorder:
    def exact():
        pass
    def exact():
        pass
    def exact():
        pass
    def exact():
        pass
    def exact():
        pass    

class Secondorder:
    def homogeneous():
        print("\n\nGiven the form:\nay\" + by' + cy = 0\n")
        a = int(input("Input your 'a' value: "))
        b = int(input("Input your 'b' value: "))
        c = int(input("Input your 'c' value: "))
                
        try:
            x1 = -b+cmath.sqrt((b**2)-(4*a*c))/(2*a)
            x2 = -b-cmath.sqrt((b**2)-(4*a*c))/(2*a)
        except:
            print("Error")
           
        try:
            x1 = str(x1).replace("+0j","")
            x2 = str(x2).replace("+0j","")
        except:
            print("Error")
            
        solution_list = [x1,x2]
        return solution_list
    def homogeneous_output():
        my_list = homogenous()
        x1 = my_list[0]
        x2 = my_list[1]
        if x1 != x2 and "j" not in str(x1):
            print("The general form of a solution for this is:\ny=c1e^(at)+c2e^(bt)")
            print(f"Your first solution is c1(e^(({x1})t))")
            print(f"Your second solution is c2(e^(({x2})t))")
            print(f"Using the superposition principle, the general solution to the provided differential equation is:\nc1(e^(({x1})t))+c2(e^(({x2})t))")
        if x1 == x2:
            print("The general form of a solution for this is:\ny=c1e^(at)+c2te^(bt)")
            print(f"Your first solution is c1(e^(({x1})t))")
            print(f"Your second solution is c2t(e^(({x1})t))")
            print(f"Using the superposition principle, the general solution to the provided differential equation is:\nc1(e^(({x1})t))+c2t(e^(({x1})t))")
        if "j" in str(x1):
            temp = str(x1).split("+")
            temp[1] = temp[1].replace("j","")
            print("The general form of a solution for this is:\n(e^(at))[c1sin(bt)+c2cos(bt)]")
            print(f"Your solution is:\n(e^({temp[0]}t))[c1sin({temp[1]}t)+c2cos({temp[1]}t)]")
    def nonhomogeneous():
        
    
class Laplace:
    pass
    
def main():
    Secondorder.homogeneous()
    
    order = int(input("What order is your differential equation? (1, 2, ?) [Respond with a question mark if you don't understand the question!]:\n"))
    if (order == 1):
        print("")
    if (order == 2):
        print("Second order equations to be solved will be in the form:\nay\" + by' + cy = f(x)\n")
        function = int(input("Input f(x): "))
        if function == 0:
            Secondorder.homogeneous()
            Secondorder.homogeneous_output()
        else:
            Secondorder.nonhomogeneous()
    if (order == 3):
        print("stuff")
        
    return 0

main()
