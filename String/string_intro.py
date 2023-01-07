#create a string variable

a="hello"

b="hello "

#How do we compare these two strings?

#We can use == sign to compare two string values

print(a==b) #fa;se spaces matter

c="Hello"

print(a==c) #false because the cases of the strings are important


print(a=="hello") #True

print('hello'=="hello") #true

#String is one of the built in data types in python
#And string values are immutable they dont change their valuue unless reassigned

email_template = ''' Hello Techtorial,

I will not be able to attend class today, because
of some personal reasons. 
Thanks, 
Name LastName
'''
print(email_template)
a=765
a =str(a)
print(a[2])