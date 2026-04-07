favorite_foods = ('matooke', 'rice', 'millet')
print(favorite_foods[0]) #Accessing the first item in the tuple
print(favorite_foods[1]) #Accessing the second item in the tuple
print(favorite_foods[2]) #Accessing the third item in the tuple
print(favorite_foods[-1]) #Accessing the last item in the tuple
# favorite_foods[0] = 'posho' # This will raise an error because tuples are immutable

numbers = (3, 7, 3, 9, 3) 
print(len(numbers))
print(numbers.count(3)) #Count how many times 3 appears in the tuple
print(numbers.index(7))