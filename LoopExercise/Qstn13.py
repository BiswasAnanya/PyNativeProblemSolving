#  Write a loop to find the factorial of any number

num= 45
result=1
if num ==0:
    print("The Factorial of zero is 1")
elif num <0:
    print("Negative number doesn't have factorials.")
else:
    for i in range(num,0,-1):
        result= result*i
    print("Factorial of the given number is:",result)