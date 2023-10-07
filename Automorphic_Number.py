def checkAuto(a): 
    if a < 0: a = -a 
    squareNum = a*a 
    temp = a 
    count = 0
    while temp != 0: 
        count += 1
        temp = int(temp/10) 
    lastDigit = squareNum%pow(10, count) 
    if lastDigit == a: 
        return "Automorphic Number"
    else:  
        return "Not an Automorphic Number"
num = int(input())
print(checkAuto(num))