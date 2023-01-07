#WE can ask the user to enter a string and remove the spaces in the beginning and at the end of the string


str="                    Techtorial               "

print(str)
print(str.strip())

# IN strip mehtod we can provide a character and it will remove that character from the beginning and end of the string

#Let's write a phone number in the middle of hastags

phone_num="####2247174751######"

print(phone_num.strip("#"))

#we can use strip method with multiple characters as well

web_site="www.techtorial.com"

#I want ot get domain name

print(web_site.strip("w.com"))