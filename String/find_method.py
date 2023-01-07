
#  012345
a="Python"


#Accessing the element
#We are using index number of a character to access element

print(a[2])  #t

#I need to learn position of the letter h
#TO learn index number of a given character
#we use find method 

print(a.find("h")) #3
#return type of find method is integer

print(type(a.find("h")))

var2="encapsulation is good for data hiding"

print(var2.find("a"))

#even character is repeating throughout the string will return index number of first


#rfind() method
#This method will help us to get
#last position of a given character

print(var2.rfind("a")) #29

var3="Python Python"

print(var3.find("hon")) #3
#even multiple characters are passed as an argument to find method
#it will return the index number of first character


print(var3.find("Peter")) #-1
#When the argument given in the find method
#doesnt exist in the string, find method will return -1

print(var3.find("z")) #-1


print(var3.rfind("th")) #9





