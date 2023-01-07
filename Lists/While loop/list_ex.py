#Create a program to find second largest element
#from the list
l=[1,99,100,110,200,34,99,199]

highest=l[0]
second_highest=l[0]
for element in l:
    if element>highest:
        second_highest=highest
        highest=element
    elif element>second_highest:
        second_highest= element

print(f"biggest element in the list is {highest}")
print(f"second largest element in the list is {second_highest}")
