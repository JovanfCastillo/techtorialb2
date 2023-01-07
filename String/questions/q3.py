#Give a string, return a new a string made of 3
#copies of the first 2 characters of the original string
#The string may be any length
#IF there are fewer than 2 characters
#use whater is there

#"Hello"-->"HeHeHe"


print("enter a string")

var=input()

first2=var[:2]
result=first2*3 #multiplies string times 3
print(result)