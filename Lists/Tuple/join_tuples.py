t1=(0,1,2)
t2=("new1","new2")

t3=t2+t1

print(type(t3)) #class tuple
print(t1) #(0,1,2)
print(t2) #new1, new2
print(t3) #(0,1,2,new1,new2)

items=("pen","pencil","eraser","keyboard")

new_t=items*3

print(new_t)
