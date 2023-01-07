
d1={
	"brand":"Apple",
	"model":"macbook pro",
	"year": 2021

}

#how can you access the values from this dict?

#Using the value of keys we can access the elements

print(d1["brand"]) #apple

print(d1.get("brand")) #apple

print(d1.get("new")) #none

#The difference between accessing the element using get method
#square brackets is when square brackes used and key is
#not present in the dictionary it will generate Key Error.
#However in get method, we wont see this error even key
#is not present in the dictionary.