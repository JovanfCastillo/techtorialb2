
bool1=True
bool2=False

print(bool1 and bool2) #False

print(bool1 and not bool2) #True

print(bool1 or bool2) #True

print(not bool1 or bool2) #False

#Only kids who are age of 11 and younger can participate 

age_of_kid,required_age=7,11

#Create a program to display if this kid can join the event
 
can_participate=age_of_kid<=required_age
print("The kid can participate", can_participate)


#Veera wants lose 10 pounds in one month. 
# There are multiple conditions to lose 10 pounds in a month 
# Veera needs to walk 10000 steps daily  OR needs to run at least 4 miles a day. 
# and Addition to those , Veera needs eat less than 1500 calories daily. 
# We should create a program to calculate if Veera can loose weight or not.

daily_calories=1600
running_distance=4
walking_steps=7000

can_lose=(running_distance>=4 or walking_steps>=10000) and daily_calories<1500
print("Veera can lose 10 pounds in one month",can_lose)




sold_tickets=1000
max_capacity=2000
print("Stadium has seats",max_capacity>sold_tickets)




