obj_in_cl=("camera","table","light","laptop","screen")


#line above is called packing a variable in python

#we can also unpack variables in tuple

#How many elements does the tuple above has?
#5
 
item1,item2,item3,item4,item5=obj_in_cl
print(item1)
print(item2)
print(item3)
print(item4)
print(item5)

obj_in_cl=("camera","table","light","laptop","screen")

#I want to unpack these variables with 3 variable total
#using star get the rest of elements and pack it into the list

i1,i2,*i3=obj_in_cl

print(f"The value of i1 is {i1} and the date type of i1 is",type(i1))
print(f"The value of i2 is {i2} and the date type of i2 is",type(i2))
print(f"The value of i3 is {i3} and the date type of i3 is",type(i3))

obj_in_cl=("camera","table","light","laptop","screen")
t1,*t2,t3=obj_in_cl #t2 table light laptop

print(t2)








