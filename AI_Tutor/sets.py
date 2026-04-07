#Create two sets — morning_patients and afternoon_patients — with some names overlapping. Then print the union, intersection, and difference. 
#Union == all unique patients from both sets
#Intersection == patients that are in both sets
#Difference == patients that are in the first set but not the second set

allergies = {'peanuts', 'mushrooms', 'mayonnaise', 'peanuts'} #Create a set of allergies, including a duplicate 'peanuts'
print(allergies) #Print the set of allergies to show that duplicates are not stored 

morning_patients = {'alice', 'bob', 'charles', 'robert', 'diana'}
evening_patients = {'diana', 'edward', 'frank', 'charles', 'george'}
union_patients = morning_patients.union(evening_patients) #Find the union of morning and evening patients)
intersection_patients = morning_patients.intersection(evening_patients) #Find the intersection of morning and evening patients
difference_patients = morning_patients.difference(evening_patients) #Find the difference of morning and evening patients

#Alternatively:
union_patients = morning_patients | evening_patients #Using the set union operator | to find the union of morning and evening patients
intersection_patients = morning_patients & evening_patients #Using the set intersection operator & to find the intersection of morning and evening patients
difference_patients = morning_patients - evening_patients #Using the set difference operator - to find the difference of morning and evening patients

print(f"Union of patients: {union_patients}") #Print the union of patients
print(f"Intersection of patients: {intersection_patients}") #Print the intersection of patients
print(f"Difference of patients: {difference_patients}") #Print the difference of patients
