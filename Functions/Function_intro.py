def first_method():
    print("hello world")


#Functuons will only get executed when they are called
#To call the methods we can use their name

first_method()

#Since no data has been returned from the method the code below
#will execute the first_method and then will print none
print(first_method())


def second_method():
    return "From second method"

second_method()


#In the print statement below, the code will print the data coming
#from the function

print(second_method())

