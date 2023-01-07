#Ask user to enter a password
# If the password doesn't have any uppercase or doesn't have any lower
#bother upper and lower case letters
# If it contains both upper and lower case letters
#print True otherwise print False

print("enter a password")
password=input()
#variabel lower is lower case version of password
lower=password.lower()
upper=password.upper()
#How can i understand if there is alower case in this password?

#This password should be equal to its upper case version 
#Therefore i can say if this password is not equal to its lower case version it means it contains some lower cases
isThereLower=password!=upper
isThereUpper=password!=lower

is_valid= isThereLower and isThereLower

print(is_valid)