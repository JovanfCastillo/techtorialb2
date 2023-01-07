#Create a method that takes one dict and one value as parameter
#Check if the given value exists in the dictionary
#If the given value exist in dictionary return True, return False.


def is_value_present(dict,value1):
    #How can i get all values from dictionary?
    #values()
    return value1 in dict.values()

d={
    "name":"ye",
    "last_name":"t",
    "school_num":390,
}

print(is_value_present(d,390)) #truuue
print(is_value_present(d,210)) #false