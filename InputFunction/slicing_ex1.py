#Ask user to enter a string and print a rotated left 2 version.
#Where the first 2 characters of the string are moved to the end
#hello --> lloHe
print("please enter a word")
Regular_word=input()
first_two=Regular_word[:2]
print(Regular_word[2:]+first_two)