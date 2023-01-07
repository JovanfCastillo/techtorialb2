list= [2,5,True,"s",2.5]

#print(list[5])  #Index error list index out of range

print(type(list[3])) #class string

#WE are getting a range of elements from the list
#therefore it will be another list

print(type(list[1:4]))  #Class LIST

list[1:2]=["new1,new2"]
print(list[2]) #new2


list= [2,5,True,"s",2.5]
list[1]=["new1","new2"]
print(type(list[1])) #class list

print(list[1][0])   #new1


print(list[-1]) #2.5


list= [2,5,True,"s",2.5]
index=0
while index<len(list):
    print(list[index])
    index=index+1
