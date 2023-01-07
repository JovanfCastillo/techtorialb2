#Given a string, if the first or last characters are 'x'
#Print the string without those 'x' characters, and
#otherwise return the string unchanged

#"xHix"--> "Hi"


print("enter string")

var=input()

first_ch=var[0]
last_ch=var[len(var)-1]

first_ch=first_ch.replace("x","")
last_ch=last_ch.replace("x",'')

#i need to get part of the string where first and last letters are not included

var=var[1:len(var)-1]
var=first_ch+var+last_ch
print(var)