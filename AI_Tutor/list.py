#Create a list of 3 medications, then: 1. Change the first one to a different mdication. 2. Add a fourth medication using .append(). 3. Print the list .
medications = ['paracetamol', 'aspirin', 'ibuprofen']
medications[0] = 'amoxicillin' #Changing the first medication to a different one
medications.append('moxifloxacin') #Adding a fourth medication using .append()
print(medications) #Printing the list of medications
# medications.pop(2) #Removing the third medication from the list
# print(f"Updated list of medications: {medications}") #Printing the updated list of medications
# medications.pop(2) #Removing ibuprofen from the list using .remove()
# print(f"Updated list of medications: {medications}") #Printing the updated list of medications
# medications.pop() #Removing the last medication from the list using .pop()
# print(f"Updated list of medications: {medications}")  
medications.remove('aspirin') #Removing aspirin from the list using .remove()
print(f"Updated list of medications: {medications}") #Printing the updated list of medications
print('removed medication: aspirin') #Printing the removed medication

active_meds = ["amoxicillin", "aspirin", "ibuprofen"]
discontinued_meds = []

stopped = active_meds.pop(1)       # removes 'aspirin', hands it to you
discontinued_meds.append(stopped)   # now you log it

print(active_meds)        # ['amoxicillin', 'ibuprofen']
print(discontinued_meds)  # ['aspirin']