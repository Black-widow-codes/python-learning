# To display five asterisks on a single line. Each asterisk must be separated by a space. You must use a while loop to solve this program.

string = ""
index = 0

while index < 5:
    index += 1
    string += " *"

print(string)

# To display the numbers 1 to 5 on separate lines.

regular_counter = 0

while regular_counter < 5:
    regular_counter += 1
    print(f"attempt: {regular_counter}")

for index in range(5):
    print(index+1)