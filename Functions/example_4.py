#Create a method to check if a given string is palindrome
#palindrome string means when the string equals its reversed version.
#hannah civic, racecar
#How can i make this method not case sensitive

def is_palindrome(s1):
    reversed=s1[::-1]
    reversed=reversed.lower()
    s1=s1.lower()
    return reversed==s1

print(is_palindrome("Hannah"))