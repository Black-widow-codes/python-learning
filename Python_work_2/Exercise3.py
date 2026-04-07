#Write a program that asks the user to enter their age. 
# Print True if the age is greater than 18, otherwise print False.

# age = input("enter your age: ")
# print(age)

# age = int(input("enter your age: "))
# print(age>18)

# first = float(input("Enter first number: "))  #I used float() to allow decimal inputs.
# second = float(input("Enter second number: "))

# print(first < second)

# first = int(input("Enter first number: "))
# second = int(input("Enter second number: "))
# print(second < first)

# x = 10
# print(x == 10)
# print(x != 5)
# print(x >= 7)

# number = int(input('Enter a number: '))

# if number > 0:
#     print(f"{number} is postive number.")

# rate = float(input("Enter hourly pay rate: "))

# if rate < 7.50:
#     print("Error: Hourly pay rate can not be less than $7.50.")

# text = input("enter a string: ")
# if text != "":
#     print(f"You have entered: {text}")

# score = int(input("Enter your score: "))

# if score >= 90:   #I used comparison operators (> 0) to test positivity.
#     print(f"Your score of {score} is excellent.")

# integer = int(input("Enter an integer: "))

# if integer % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

# username = str(input("Enter your username: "))
# if username == "":
#     print("You must enter username")
# else:
#     print(f"Welcome {username}")

# password = input("Enter your password: ")
# if password == "python123":
#     print("Access granted")
# else:
#     print("Access denied")

# rate = float(input("Enter hourly pay rate: "))
# hours = float(input("Enter hours worked: "))

# gross_pay = rate * hours

# if gross_pay <= 300.00:
#     tax_rate = 0.10
# else:
#     tax_rate = 0.12

# withholding_tax = gross_pay * tax_rate
# net_pay = gross_pay - withholding_tax
# print(f"Gross pay: ${gross_pay: .2f}")
# print(f"withholding tax: ${withholding_tax: .2f}")
# print(f"Net pay: ${net_pay: .2f}")


# years = float(input("Enter number of years money was left in the bank: "))

# if years > 5:
#     print("Interest rate is 7.5%")
# else:
#     print("Interest rate is 5.4%")

# grade = input("Enter your grade: ")

# if grade == "A":
#     print(f"Excellent for {grade}")

# grade = input("Enter a grade (A, B, C, D, F): ").upper()

# if grade == "A":
#     print("Excellent")
# elif grade == "B":
#     print("Good")
# elif grade == "C":
#     print("Average")
# elif grade == "D":
#     print("Poor")
# elif grade == "F":
#     print("Fail")
# else:
#     print("Invalid grade")

# number = int(input("Enter a number: "))

# if number > 0:
#     if number % 2 == 0:
#         print("Positive and Even")
#     else:
#         print("Positive and Odd")
# elif number < 0:
#     print("Negative number")
# else:
#     print("Zero")


# year = int(input("Enter a year: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print("Leap year")
# else:
#     print("Not a leap year")

first = float(input("Enter first number: "))
second = float(input("Enter second number: "))

if first > 0 and second > 0:
    print("Both positive")
elif first > 0 or second > 0:
    print("At least one positive")
else:
    print("No positives")







