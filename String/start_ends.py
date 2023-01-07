#ASk user to give two different string values
#and print tru if the second string starts with last two characters
#of the first string or print True
#if the first string starts with first two characters of the second string 

print("enter first string")
s=input()

print("enter second string")
s2=input()

# I need last 2 characters of the first string 
last_two=s[-2:]

condition1=s2.startswith(last_two)


first_two=s2[:2]
condtion2=s.startswith(first_two)

print(condition1 or condtion2)