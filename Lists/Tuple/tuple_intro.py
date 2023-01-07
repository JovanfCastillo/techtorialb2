
#How can i create tuple with one item in it?

tupl=("class")

print(type(tupl))  #this line will print class str


tl=("class",)    #this makes it a tuple with one element

print(type(tl))

#How do we access the elements from the tuple?

t=('c','b','d',1,2,3,4)
#print all elements in this tuple in a different line?

for e in t:
    print(e)

#Do negative indexes work for tuple as well?
#Yes it does 
print("Negative index 5 is ",t[2:5]) 

print(type(t[2:5])) #tuple

print(type(t[-4])) #integer

print(t[2:3]) #d

print(type(t[2:3])) #tuple

#How could we check if certain items exist in a tuple?



if "d" in t:
    print("d is in the tuple")
else:
    print("d is not in the tuple")


print("d" not in t)


#Line below will generate a type error.
#t[2:6]=("c","b","new1","new2","new3","new4")
#print(t) 

