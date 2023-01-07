#Remove suffix -> will remove it from end of the string
#remove prefix will remove it from the beginning of the string

s="Hello World"
print(s.removeprefix("World")) #Hello World

print(s.removeprefix("Hello")) #_World

print(s.removesuffix("World")) #Hello_

print(s.removeprefix("olleH")) #Hello World

#unlike the strip method, in remove suffix and prefix method
#order of the characters are important

print(s.strip("elloH"))

