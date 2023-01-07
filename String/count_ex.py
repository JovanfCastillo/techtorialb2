#Ask user to give a string filled with cats and dogs texts
#From the given string   if the number of dogs and cats is the same print True
#other wise print false


print("Give a string consists of dog and cat words")

str=input()

count_of_dogs=str.count("dog")

count_of_cats=str.count("cat")

Same_counts=count_of_cats==count_of_dogs

print(Same_counts)