"""Write a function called say_hello() that prints "Hello World".
Call the function to see the result."""

# def say_hello():
#     print("Hello World")

# say_hello()

# def print_name(name):
#     print(f"Hello {name}")

# print_name("bryan")

# Write a function square(n) that returns the square of n.
# def square(n):
#     return n * n
# print(square(2))
# print(square(3))
# print(f"square of 5 is {square(5)}")
# print(f"The sqaure of 10 is {square(10)}")


def max_of_two(x, y):
    if x > y:
        return x
    else:
        return y


print(f"The maximum of 10 and 20 is {max_of_two(10, 20)}")
print(f"The maximum of 30 and 20 is {max_of_two(30, 20)}")
print(f"The maximum of 40 and 50 is {max_of_two(40, 50)}")

# Write a function is_even(n) that returns True if n is even, otherwise False.


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


print(f"Is 3 even? {is_even(3)}")
print(f"Is 10 even? {is_even(10)}")
print(f"Is 15 even? {is_even(15)}")

# Define a function add(x, y) that returns the sum of two numbers.


def add(x, y):
    return x + y


print(f"-3 + -1 = {add(-3, -1)} ")
print(f"3.5 + -1 = {add(3.5, -1)}")
print(f"3.5 + 2.5 = {add(3.5, 2.5)}")

x = 3
y = 2
print(x + y)
