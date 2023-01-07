#Ask user to enter a string
#if the given string contains any duplicted letter
#print string has duplicated letter
#otherwise print string consisits of unique letters.

print("enter a string")
str=input()

#I have to check count of each letter in the string
#if any count of the letter is bigger than 1 it means
#this string has a duplicated letter

index=0
#On the line below i asssume string doesnt have
#any duplicated letter
is_duplicated=False
while index<len(str):
    print(str[index])
    #my goal is to find if str[index] is unique or duplicated
    if str.count(str[index])>1:
        is_duplicated=True
    index+=1

if is_duplicated:
    print(f"{str} contains duplicated letters")
elif not is_duplicated:
    print(f"{str} doesnt contain any duplicated letter")
