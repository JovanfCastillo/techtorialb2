#.values(), .keys()

d1={
	"brand":"Apple",
	"model":"macbook pro",
	"year": 2021
}

print(d1.values())
print(type(d1.values())) #dict values

print(d1.keys())

print(d1.keys())
print(type(d1.keys())) #dict keys

#to get all values from the dict

for v in d1.values():
    print("value of v",v, "type of value", type(v))


#we can get key and value at the same time using loop
#we need to use items method

for k, v in d1.items():
    print("Key is",k,"and value is",v)
    