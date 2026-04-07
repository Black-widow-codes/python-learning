def OddorEven(number): #It creates a function called OddorEven. checks if the number is odd or even
    if number % 2 == 0: #divisor function checks to see if the number is odd or even
        print(f"num {number} is even") #f-string - It lets you insert variables inside {}.
    else:               #if the number is not even, it must be odd
        print(f"number {number} is odd")

def square(number):  #It creates a function called square. It takes a number as an argument and computes the square of that number.
    return number ** 2 #computes square. return sends a value back to the caller

def cube(number):  #It creates a function called cube. It takes a number as an argument and computes the cube of that number.
    return number ** 3 #computes cube

num = int(input("Enter a number between 1 and 10: "))
choice = (int(input("Enter your choice between 1 and 3: "))) #int converts input to integer
print(f"You have selected choice {choice}")

match choice: #compares values against cases
    case 1:    
        OddorEven(num)   #calls the OddorEven function and passes the num variable as an argument. The function will determine if the number is odd or even and print the result.
    case 2: 
        result = square(num) #calls the square function and passes the num variable as an argument. The function will compute the square of the number and return the result, which is stored in the variable result.
        print(f"square of {num} is {result}.")
    case 3:
        result = cube(num)  #
        print(f"cube of {num} is {result}.")
    case _:                                       #is a default case
        print("You have entered an incorrect choice.")

