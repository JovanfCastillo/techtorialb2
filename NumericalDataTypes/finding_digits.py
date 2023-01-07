
a=681

#FInd the multiplication of digits of number a
#Solution should work for every three digit number
#multiply the each digit of number a

print(32//10)

#when the integer divide number with 10 it will get rid of the 
#las digit of the number
#when i find the remainder with 10 i get the last digit of the number 

print((a%10)*(a//10%10)*(a//100))

last_digit= a% 10

first_two_digits= a//10

middle_digit= first_two_digits%10

first_digit= first_two_digits//10

print(last_digit*middle_digit*first_digit)

#create a function  to find each digit of the given number 
#create a program to find each digit of the number and sort them



