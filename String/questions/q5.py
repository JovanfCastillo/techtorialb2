#Given a string, print True if "bad" appears starting at 
#index 0 or 1 in the string such as with "badxxx" or "xbadxxx"
#The string may be any length including 0

print("enter a string")
str1=input()

#find ()
#find("bad") -> it will return me with the word 'bad'
#starts in the string

starting_index=str1.find("bad")
#in the question it says starting index for this word should be 1 or 0

bl= starting_index==1 or starting_index==0

print(bl)