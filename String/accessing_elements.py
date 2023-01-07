
day="saturday"

# 123456 6 will be the length of the string
#012345 will be the index of the string 

letter_4th=day[3]

print(letter_4th) # d

print(type(letter_4th)) # class str


#IF the index number we are trying to access is bigger than last index
#Number in the string it will throw index out of range error
#print(day[14])

#From the given string print out the last 2 letters

print(day[len(day)-2], day[len(day)-1]) #ay 


#When you use plus sign between 2 string values, it is called concatenation

str1="Hello"
str2="World"

#Concatenate two string above

print(str1+str2)

print(len("text")) #4

print("text"[2]) # x

#len() you can always use with any string and find out the length of the string
#relation between length of the string and index numbers is
#Last index of the string is one smaller than length of the string 



a=789

print(type(a))

#print(a[1]) Type error int object is not subscriptable

#print(len(a)) #Type error object of type int has no len()

#Function length works with every data type that uses index numbers

b=5.4

#print(b[1]) Type error float object is not subscriptable
#flot has no len()
#complex is not subscriptable