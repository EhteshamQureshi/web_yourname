#! /usr/bin/python
mystring = "this is a variable"
mylist = ['a', 'b', 3, 4] # Here we have declared list.Lists are used to store multiple items in a single variable.
mytuple = ('a', 'b', 3, 4) # tuple is a collection. Tuples are used to store multiple items in a single variable.
mymarks = {"webProg":80, "OOSD":70, "POC":68, "NOS": 50} #Sets are used to store multiple items in a single variable. Sets are written with curly brackets.
#sequence
myset = set("this is a book") #To intialize a set with values, you can pass in a list to set().
#list operations
print(mylist) # print statement is used to print text or variables
mylist.insert(2,'c')#To insert a list item at a specified index, use the insert() method. The insert() method inserts an item at the specified index:
mylist.append(5)#append() method is used to add an item at the end of the list
print(mylist) # print value of my list on console
#typle operations
print(mytuple[0]) #We can access tuple items by referring to the index number, inside square brackets:
print(mytuple[1])  #along with print statement we can accrss the specific tuple item and print it.
#string operations
print (mystring[::3])
#dictionary operations
print(mymarks['webProg']) #Prints the value of single item webProg
print(mymarks.keys()) #Prints all keys for mymarks
print(mymarks.values()) #Prints all values for mymarks
#A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).
for key in mymarks.keys():# This loop will interate through teh mymarks set one by one and print till the last item
 print("Key: ", key, " Value: ", mymarks[key])

print(myset) #This will print myset Sets are unordered, that is why we are not sure in which order the items will appear.