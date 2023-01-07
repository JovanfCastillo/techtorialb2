
#Find how many word does the given string contain?
#techtorial academy -> 2
#python is a programming language -> 5

#space is seperating words from each other

print("enter a sentence")
sentence=input()
l3=sentence.split(" ")
print(l3)


count_of_words=len(l3)
print(count_of_words)


#Second solution
#count of spaces+1 
count_of_spaces=sentence.count(" ")
print(count_of_spaces+1)








