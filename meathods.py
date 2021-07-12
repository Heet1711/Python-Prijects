#lists

fruits = ["Apple", "Banana", "Pineapple"]

# To access list Items
print(fruits) #prints whole list
print(fruits[1]) #to access a particular element from list (indexing)
print(fruits[-1]) # negative indexing
print(fruits[1:3]) # to access more the onr element at the same time (reang indexing)
print(len(fruits)) #prints the length of list

# to check if the particular element exists in the list
if "Banana" in fruits:
    print("true")

# insert elements in the list
fruits.insert(2, "kiwi")
fruits.append() #adds element to the end of the list
fruits.extend() #to merge two lists

# remove elements from list
fruits.remove() 
fruits.pop(2) #removes the element with specifis index

# to clear the list
fruits.clear()


#Ttpple
mytupple = ("apple", "Banana", "kiwi")
print(len(mytupple)) #Prints the length of the tupple
print(mytupple[1]) #Accessing the tupple elements by its index
print(mytupple[1:3]) #range indexing 

# to check if the particular element exists in the tupple
if "Banana" in mytupple:
    print("true")

#sets
myset = {"Apple", "Banana", "Mango"}
print(len(myset)) #prints the length if the set

# Adding an element to the set
myset.add("orange")
myset.update() #to add elements fron another set

#removing an element fron set
myset.remove("Mango")
myset.clear() # Delets all elements of the set
del myset #Delets the complete set


#Dictionary
mydict = {"fruits": "Banana", "Vegetables": "Potato"}

print(mydict["fruits"]) #Prints the value of fruits from the dictionary
print(len(midict)) #Prints the length of the dictionary

#to print the keys from the dictionary
x = mydict.keys()
print(x)
mydict["color"] = "Black"

#to get values from dictionary
x = mydict.values() 
print(x)

#removing elements from the dictionary
mydict.pop("Fruits")
del mydict # delets the dictionary 
mydict.clear() #to clear the dictionary
