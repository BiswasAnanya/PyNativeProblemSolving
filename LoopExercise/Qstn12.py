# Display Fibonacci series up to 10 terms

num1= 0
num2= 1
count = 0

while count<10:
    print(num1, end=" ")
    temp= num1+num2
    num1=num2
    num2=temp
    count+=1
