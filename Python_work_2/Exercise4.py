#To repeatedly prompt for a number and sum it. When the sum just exceeds 100, 
# stop the prompting and display the sum at the end. You must not display the sum while the user in typing in numbers. 
# (You do not need a counter but you will need some way of terminating the loop)

# total = 0

# while True:
#     number = float(input("Enter a number: "))
#     total += number

#     if total > 100:
#         break

# print("Final sum:", total)

# #Same as the previous question but additionally displays the average of the numbers when the loop terminates. 
# # You will need a counter but not as a loop terminator.
# counter = 0
# total = 0

# while True:
#     number = float(input("Enter a number: "))
#     total += number
#     counter += 1

#     if total > 100:
#         break

# average = total / counter
# print("Final sum:", total)
# print("Average:", average)

#To display the sum of all the multiples of 3 between 1000000 and 2000000. (
# Answer = 499, 999, 500, 000). If you suspect that a value might be larger than 2 billion (as is the case here),
#  then the type of sum should be a long and not an int. [Hint: like the C (currency) and the F (decimal) format specifiers, 
# there is also a N specifier]

total = 0
number = 1000000

while True:
    if number % 3 == 0:
        total += number

    number += 1

    if number > 2000000:
        break

print(f"Sum: {total:,}")

#A conversion table of Celsius to Fahrenheit temperature. 
# The table must start with 100 Celsius and end at 0 Celsius with decrements of 10. 
# (Fahrenheit = 9/5 * Celsius + 32). Your table must have a suitable header and the 
# values in the table must be right-align like the output of question 11.

