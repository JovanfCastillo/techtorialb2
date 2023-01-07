nums=[1,2,3,1,2,3,4,2,2,2,2,2]

#remove all number 2's from this list

#when i remove the element from the list i should make
#an increase in the index number
index=0
while index<len(nums):
    if nums[index]==2:
        nums.remove(2)
        index-=1
    index+=1



print(nums)
