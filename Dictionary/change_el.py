l=[1,2,3]

#If i wanted to change value of second element what 
#would i do?
l[1]="new value"
print(l)

d1={
	"brand":"Apple",
	"model":"macbook pro",
	"year": 2021

}


#i want to change the model of the laptop
d1["model"]="Macbook Air"

d1["new"]="macbook pro"
print(d1)

#Can i change the elements in different way?
#update method to change the value of elements in a dictionary
#update method takes a dictionary as paremeter and changes
#the value of the element




d1.update({"year":2022})
print(d1)

d1.update({"charging-port":"usb"})
print(d1)