#create a method taht will return lowest common factor of two given numbers
#lowest common factor is lowest number that can be divided by two given numbers

#LCM for 4 and 6 is 12
#4 and 8 lcm is 8
#for 6 and 8 ->24

def lcm(n1,n2):
    #we need to start from either n1 or n2 and we should increase
    #the number until we can divide
    lowest_c=n1
    #because i want to increase these two numbers cant divide
    while (lowest_c%n1!=0 or lowest_c%n2!=0):
        lowest_c+=1
    return lowest_c

print(lcm(4,6))