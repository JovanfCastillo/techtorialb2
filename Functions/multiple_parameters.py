#let's create a function that takes multiple numbers
#as a parameter and returns multiplication of those numbers.

def find_multiplication(*numbers):
    #This numbers variable should be treated as a tuple because it is a tuple
    multi=1
    for element in numbers:
        multi*=element
    print(multi)



find_multiplication(1,2,4,5,3)
