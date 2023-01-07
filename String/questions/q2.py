#Given a string, print true if the first 2 characters in the string also appeart at
#the end of the string, such as with "edited"
#ed-> true
#edit -> false

print("enter a string")

str1=input()

#first 2 character and last 2 character should be same 
#I need to compare first 2 characters and last 2 characters

#first2chars==last2chars

#How can i find first 2 and last 2 characters

first2chars= str1[:2]      #first two characters


bl=str1.endswith(first2chars)
print(bl)





#bl=str1.endswith()










