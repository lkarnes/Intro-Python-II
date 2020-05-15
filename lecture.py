"""
store 

The Dugout 
1 running 
2 baseball 
3 basketball
4 exit
"""

from lecture2 import Department

class Store: 
    def __init__(self, name, departments):
        self.name = name
        self.departments = []
        for d in departments: 
            department = Department(d)
            self.departments.append(department)
        
    def __str__(self):
        output = ""
        output += self.name + '\n'
        for index, department in enumerate(self.departments):
            output += str(index+1) + '.' + str(department) + "\n" 
        return output
    
        
store = Store('The Dugout', ["Running", "Baseball", "Basketball", ])

selection = 0
print(store)


while selection != 4:
    selection = input("Select the Number of the Department. ")
    try:
        selection = int(selection)  
        if selection >= 1 and selection < len(store.departments)+1:
            print(f'the user selected {store.departments[selection-1]}')
        else:
            print('choose from given choices.')
    except ValueError:
        print('choose a number not an empty string or letter')
print ("!!!thankyou for shopping with us!!!!")