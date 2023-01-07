print("enter a starting point")
starting_num=int(input())
print("ending point point")
end_num=int(input())

#i have to check every number in this range to understand
#if they are prime number
#I have check all possible dividers of a number
#and other 1 and itself none of the possible
#divider should be able to divide that 
#number to make it a prime number

#11
#what is the possible dividers for this 
#number 11?


while starting_num<=end_num:
    #instead of printing I have to find out if
    #starting_num is prime
    possible_divisor=2
    #it should range from 2 to starting_num
    #I assume on the line below that starting_num
    #is a prime number
    is_prime=True
    while possible_divisor<starting_num:
        #I have to check if possible divisor is an
        #actual divisor of starting num
        if starting_num%possible_divisor==0:
            is_prime=False
        possible_divisor+=1
    if is_prime and starting_num>1:
          print(f"{starting_num} is prime number")
          #this line again belongs to outer loop
    starting_num+=1




#I am able to get when numbers are not prime
#I need to print only one time if they are prime or not
