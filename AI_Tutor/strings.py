full_name = ('bryan', 'kaye')
print(full_name.count('bryan')) #Count how many times 'bryan' appears in the tuple
print(full_name.count('kaye')) #Count how many times 'kaye' appears in the tuple
print(full_name.index('bryan')) #Find the index of 'bryan'
print(full_name[0].upper()) #Convert the first element to uppercase
print(full_name[1].upper()) #Convert the second element to uppercase
print(full_name[0].lower()) #Convert the first element to lowercase
print(full_name[1].lower()) #Convert the second element to lowercase

name = 'mississippi'
print(name.count('s')) #Count how many times 's' appears in the string
print(name.count('p')) #Count how many times 'p' appears in the string
print(name.find('p')) #Find the index of the first occurrence of 'p'
print(name.find('z')) #Returns -1 if the substring is not found
print(name.index('z')) #Raises a ValueError if the substring is not found