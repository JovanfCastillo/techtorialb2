#Create a method that takes full name as parameter
#and returns upper case version of that fullname.

def upper_case_name(full_name):
    return full_name.upper()

#Since int object doesnt have upper method
#the code below ill return int object has no attribute upper()

#print(upper_case_name(5))

print(upper_case_name("john wick"))

#can only take on parametere at a time #john wick, saul goodman

#When the methods are create we can call it as many times as necessary
