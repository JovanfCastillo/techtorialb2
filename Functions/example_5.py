#Create a method that will take one list as a parameter and one positive
#interger index as a parameter.Return the negative index for given positive index number.

#we have to understand relation between negative and positive indexes.
#p,y,t,h,o,n
#0,1,2,3,4,5
#654321 (negatives)

def find_neg(s1,index):
    neg_index=index-len(s1)
    return neg_index
print(find_neg(["p","y","t","h","o","n"],3))