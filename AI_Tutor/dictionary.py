patient = {
    'name': 'robert johns', #Creating a dictionary called patient with keys 'name', 'age', and 'blood_type' and their corresponding values.
    'age': 30,
    'blood_type': 'A+',
    'medications': ['paracetamol', 'aspirin', 'ibuprofen']

}

print(f"Patient Name: {patient['name'].title()}") #Using an f-string to format the output with the patient's name from the dictionary and applying the .title() string method to capitalize the first letter of each word.

patient['age'] = 31
print(f"Updated Age: {patient['age']}")

patient['room_number'] = 201
print(f"Patient Details: {patient}")
patient['medications'].append('amoxicillin') #Adding a new medication to the list of medications in the dictionary using .append()
print(f"Updated Medications: {patient['medications']}")
      
