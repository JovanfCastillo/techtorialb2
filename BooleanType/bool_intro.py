bool1= True
bool2=False

print(type(bool1)) #class 'bool'
print(type(bool2))

print(bool1)  #true
print(bool2) #false


#We are trying to use arithmetical operation
#Using a numerical value of the boolean variable
#The python make sense out of the expression below


print(bool1+6) #7

print(bool2*122) #0

# What happens when we use a comma between a number and a boolean variable

print(bool1,6) #true 6
print(bool2,6) #false 6

#How to print string and boolean in single print function?3
#Just use comma between two variable
print("The value of the bool1 is",bool1)
print("The value of the bool2 is",bool2)

a=0.25
print(bool(a))
