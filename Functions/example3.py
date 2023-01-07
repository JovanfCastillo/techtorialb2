#create a method to find a highest common factor of two given numbers
#highest common factor is a biggest common divisor of two given numbers

def highest_common_divisor(n1,n2):
    #if it can divide both numbers without any remainder
    hcf=n1
    while n1%hcf!=0 or n2%hcf!=0:
        hcf-=1
    return hcf
print(highest_common_divisor(60,24))