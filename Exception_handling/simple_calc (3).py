

#using a lookup dict to convert string to real operator 
#and then calc. 
op = {
    "+": lambda x,y: x + y,
    "-": lambda x,y: x - y,
    "*": lambda x,y: x * y,
    "/": lambda x,y: x / y,
    "%": lambda x,y: x % y,
    "**": lambda x,y: x ** y,
    "//": lambda x,y: x // y,

}
#the func takes in two numbers and an operator, then calcs
#also stores the equ in the file 'myfile.txt'
def type_in():
    try:#try and except used here to catch error safetly


        #takes in user first input number
        number1 = int(input("Enter Number: "))
        #exits the code when the users keys in -123
        
        
        #takes in user second input number
        number2 = int(input("Enter another Number: "))
        operation = input("Enter operation to be performed on the two numbers: ")
        if operation not in op.keys():
                raise ValueError("Invalid Operator:", operation )
        else:
            captured_input = f"{number1} {operation} {number2}"
            print("...saving your equation to \"myfile.txt\"")
            with open("myfile.txt", "a") as f:
                f.write(captured_input + "\n")
            print(f'{captured_input} = {op[operation](number1,number2)}')#prints out on the console

        #this writes each operation entered by the user into a text file----myfilez.txt 
        
    except ValueError as err:

        if err.args[0] == "Invalid Operator:":
             print(err.args[0], err.args[1])
             print("Insert a valid operator => ", " ".join(op.keys()),"\n")
        else:
            print("Invalid Number: input a valid number")
   
    except ZeroDivisionError:
        print("Error: you tried dividing by zero")
    except TypeError:
        print("Incorrect input: input numbers only")

#the func takes in a filename and gets the equ therein and performs the calc    
def fileread():
    # checks for file name 
    try:
        file_read = (input("Enter file name(\".txt\" file) to read from: "))

        print("file search begins")
        #opens the file 
        with open(file_read) as equation_txt:
        #loops thru each of the operation and performs all calc.
            for each_operation in equation_txt:
                each_operation_list = each_operation.split() # picks each element of the equ
                
                if " " in each_operation_list: # eliminates  " " if any
                        each_operation_list.remove(" ")
                print(f"\n{each_operation.strip()} = {op[each_operation_list[1]](int(each_operation_list[0]),int(each_operation_list[2]))}")
            
    #if the filename is not found throw an error
    except (FileNotFoundError,OSError):
        print("File not Found: Input a valid file")
    
        
    except (ValueError,IndexError):
         print("Use a valid file: file doesn't have equation ")


         
while True:
        
        try:# this code continues to take input from user
        # an calculates the outcome
        #and exits only when 123 is keyed in
    
            option_ = int(input("Press 1 to input your own equation\nPress 2 to read from file\nPress 123 to exit: "))
            if option_ == 1:
                type_in()
            elif option_ == 2:
                fileread()
            elif option_ == 123:
                break
            else:
                raise ValueError("Incorrect option: input a valid option")
        
        except ValueError as err:
             print(err.args[0])
            