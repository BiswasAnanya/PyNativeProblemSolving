# Find the sum of the series 2 +22 + 222 + 2222 + .. n terms

digit =2
n=7
sum= 0

for i in range(0,n-1):
    print(digit, end=" ")
    sum += digit
    digit= (digit*10)+2

    
print("\n",sum)
