        # You can loop through a dictionary by using a for loop.
thisdict = {
    "name": "Khalid",
    "Age" : 24,
    "Nationalit": "Somali"
}
for x in thisdict:
    print(x)
    
        # Print all values in the dictionary, one by one:
thisdict = {
    "name": "Khalid",
    "Age" : 24,
    "Nationalit": "Somali"
}
for x in thisdict.values():
    print(x)
        
        #Print all Keys() in the dictionary, one by one: 
thisdict = {
    "name": "Khalid",
    "Age" : 24,
    "Nationalit": "Somali"
}
for x in thisdict.keys():
    print(x)
   
        # Print all Item() in the dictionary, one by one: 
thisdict = {
    "name": "Khalid",
    "Age" : 24,
    "Nationalit": "Somali"
}   
for x, y in thisdict.items():
    print(x, y)