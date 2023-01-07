#WE can use pop() method to remove elements with specified
#key value
d1={
	"brand":"Apple",
	"model":"macbook pro",
	"year": 2021

}

#WE can remove the element
d1.pop("brand")
print(d1)
d1.update({"brand2":"windows"})
print(d1)




#popitem() method
#it wont take any argument
#popitem() method will remove last inserted item in a dictionary.

d1.popitem()
print(d1)


#del keyword

del d1["model"]
print(d1)

#removing all dictionary
#del d1
#print(d1) #Because object d1 is not present for python anymore

#empty all dictionary

print(d1)
d1.clear() #empty the dictionary so i will have empty dict
print(d1)

