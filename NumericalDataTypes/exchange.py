# Create a python program to give 
# most efficient exchange possible using only 
# coins 
# quarter 25 cent
# nickel 5 cents
# dime is 10 cents
# penny 1 cent
# $2.34 exchange
# 9 quarters 
# 0 dimes 
# 1 nickel 
# 4 pennies
# $1.89
# 7 quarters 1 dimes and 0 nickels 4 pennies
#create a program to give change using the least coin possible

quarter, dime, nickel, penny=.25, .10,.05,.01

exchange=10.03

#I will convert exchange to cents
total_cents=exchange*100

count_of_quarters= exchange//.25
#I give enough quarters, however how can i complete the rest of the exchange

left_after_quarters=total_cents%25
print(left_after_quarters)

#how many dimes I can exchange?

count_of_dimes=left_after_quarters//10

#i have to find what is left over after exchanging dimes
left_after_dimes=left_after_quarters%10
#I have to find how many nickel i can give
count_of_nickel=left_after_dimes//5

left_after_nickel=left_after_dimes%5

count_of_pennies=left_after_dimes%5

print("For $",exchange,"I will give",count_of_quarters,"quarters",count_of_dimes,"Dimes",count_of_nickel,"Nickels",count_of_pennies,"pennies")

