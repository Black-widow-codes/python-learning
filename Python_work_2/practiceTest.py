"""Very small and clear practice script for learning addition/subtraction.

This version is interactive-only and written step-by-step so learners
can follow the control flow easily.
"""
"""Very small and clear practice script for learning addition/subtraction.

Beginner-style: procedural code, easy-to-read variable names, and simple flow.
"""

print('Welcome to the simple calculator')
# Explain what the program does
print('Type 1 to add two whole numbers')
print('Type 2 to subtract two whole numbers')

# Ask the learner to choose an operation
choice = input('Choose operation (1 or 2): ')

# If the learner chose addition, follow the addition steps
if choice == '1':
    # Ask for two whole numbers (integers)
    num1 = input('Enter the first whole number: ')
    num2 = input('Enter the second whole number: ')

    # Convert the typed text into integers. If conversion fails, show an error.
    try:
        a = int(num1)
        b = int(num2)
    except ValueError:
        # This runs if the user typed something that is not an integer
        print('Please enter valid whole numbers (for example: 3, 10, -4)')
    else:
        # Only runs when conversion succeeded
        result = a + b  # add the two numbers
        print('The sum of', a, 'and', b, 'is', result)

# If the learner chose subtraction, follow the subtraction steps
elif choice == '2':
    # Ask for two whole numbers (integers)
    num1 = input('Enter the first whole number: ')
    num2 = input('Enter the second whole number: ')

    try:
        a = int(num1)
        b = int(num2)
    except ValueError:
        print('Please enter valid whole numbers (for example: 3, 10, -4)')
    else:
        result = a - b  # subtract the second from the first
        print(a, 'minus', b, 'equals', result)

else:
    # This runs when the learner typed something other than '1' or '2'
    print('Invalid choice. Run the script again and type 1 or 2')

