#from the two given list find all common elements

l=["n","1",1,2,3]
l2=["n",3,"1",10,11,"new","n","1",3]

#I can loop thru each element and store the common
#ones somewhere
commons=[]
for element in l:
    if element in l2:
        commons.append(element)
    
    
    #my goal is to check if that element is also 
    #present in the l2

#I can cast commone elemetns list to a set variable
#set()
common_el=set(commons)
print(common_el)

#l and l2
l=set(l)
l2=set(l2)
#intersection method to find common elements from two sets

set3=l.intersection(l2)


