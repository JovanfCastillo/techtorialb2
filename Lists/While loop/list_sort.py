list=[1,5,200,2,5,11,6,1]

#Create a program that will sort this list
#without using sort method.


#I have to find place of each element according to value
#of all other elements


for index in range(len(list)):
    #list[index]
    for k in range(index+1,len(list)):
        if list[index]>list[k]:
            temp=list[index]
            list[index]=list[k]
            list[k]=temp
print(list)
