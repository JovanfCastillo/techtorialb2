s="python"

print(s.lower())
#false because is lower method returns true
#when string has only lower case letters
print(s.lower().islower())
#true because lower method makes every character in string lower case

str="python "
print(str.islower()) #true

str.upper() #did got reasigned 

print(str.isupper())  
#false  because string is an immutable object
#therefore it will not change its value unless reassigned

print(str.upper().isupper())
#true because upper method will make everything
#upper case since i chained upper and isupper method