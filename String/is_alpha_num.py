
var1="Techtorial academy"

print(var1.isalpha())

# False

#spaces are not considered as letters
#therefore this will return false

print(var1.replace(" ","").isalpha())

#True, all characters in the string are letters

var2="weatherisniceoutside."
print(var2.isalpha())
#because of the period

#isnumeric only true when all characters are numbers

var3="123341"
print(var3.isnumeric())
#true all characters are numbers 

var5="phonenumberis9898080890"

print(var5.isalnum()) #true

var6="#777777"
print(var6.isalnum())
#false because # is neither number or letter

str1="first"

str2=""

str3="anumber7"

str4=" anumber8"


print(str1.isalnum())

print(str2.isalnum())

print(str3.isalnum())

