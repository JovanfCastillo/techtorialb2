a=(2,3,5,7,10,11,0,1)

#sort this tuple and print out the result

#Values of tuples cant be changed neither order nor value

#If i have a list I can sort it?
#I have currently a tuple but i need a list
#since this is not a list cant be sorted
#is there a possibility that i can convert(cast)
#tuple to list?

#function list() will convert(cast) tuple
#object to a list object?

l=list(a)
for index in range(len(l)):
    #list[index]
    for k in range(index+1,len(l)):
        if l[index]>l[k]:
            temp=l[index]
            l[index]=l[k]
            l[k]=temp #save the value of index create a third variable

#My end result should be still in tuple type
#Using function tuple() list can be converted into a tuple object


l=tuple(l)
print(l)
print(type(l))