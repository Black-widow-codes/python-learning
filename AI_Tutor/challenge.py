#Create a tuple called patient_info with: name, date of birth, and blood type
patient_info = ('robert johns', '2000 10 10', 'o+') 

#Create a list called medications with 3 medications the patient is taking
medications = ['paracetamol', 'aspirin', 'ibuprofen']

#Use an f-string to print: Patient: [name], DOB: [dob], Blood Type: [blood_type]
print(f"Patient Name: {patient_info[0].title()}, DOB: {patient_info[1]}, Blood Type: {patient_info[2]} ") 
#Using an f-string to format the output with the patient's information from the tuple.

#The doctor discontinues the last medication — remove it using the right method and save it to a variable called stopped
stopped = medications.pop() #Removing the last medication from the list using .pop() and saving it to a variable called stopped

#The doctor prescribes a new medication — add it to the list
medications.append('moxifloxacin') #Adding a new medication to the list using .append()

#Use an f-string to print: Discontinued: [stopped]
#Current medications: [medications]
print(f"Discontinued: {stopped}") #
print(f"Current medications: {medications}") #Using f-strings to format the output with the discontinued medication and the current list of medications.

#Use a string method to print the patient's name in uppercase
print(f"Patient Name: {patient_info[0].upper()}") 