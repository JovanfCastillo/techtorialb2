s=[10,1,3,4,5,7]
s2={10,12,100,4,5}

#Find the second lowest elemeent from the s and multiply
#with the second highest elemeent in the s2.

#The problem here is when the first element from the
#array is smallest this code wont find the 
#second lowest element
import sys

lowest_s=s[0]
#For second lowest I have to give so big number that
#any number in the array would have potential to change
#sys.maxsize is a constant value that represents biggest
#integer number
second_lowest_s=sys.maxsize

for el in s:
    if el<lowest_s:
        second_lowest_s=lowest_s
        lowest_s=el
    elif el<second_lowest_s:
        second_lowest_s=el

print(second_lowest_s)


#Before i start the loop I have to give the lowest value possible
largest_s2=-sys.maxsize-1

second_largest_s2=-sys.maxsize-1

for element in s2:
    if element>largest_s2:
        second_largest_s2=largest_s2
        largest_s2=element
    elif element>second_largest_s2:
        second_largest_s2=element
print(second_largest_s2)

print("result of multiplication is",second_largest_s2*second_lowest_s)

