s={1,2,3,4,5,6,6,6,3,4}
print(s)

#print(s[0]) #object is subscriptable, setdoesnt have indexes


#How can we learn the lenght of the list?


print(len(s))

s.add(7)
print(s)


s1={1,2,3}
s2={"n1","n2","n3"}  #{1,2,3,'n1","n2","n3"}

s1.update(s2)

print(s1)



l=[4,5,6]
s1.update(l)

print(s1)
s1.discard(4)
s1.remove(1)
print(s1)

#s1.remove({2,3,5,6}) Keyerror

#print(s1)
s1.discard({2,3,5,6})
print(s1)
s1.discard("something else")
#s1.remove("something else") key error
print(s1)