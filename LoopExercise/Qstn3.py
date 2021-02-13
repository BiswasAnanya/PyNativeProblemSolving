# Accept number from user and calculate the sum of all number between 1 and given number

n= int(input())
sum =0

for item in range(1,n+1):
    sum=item+sum
print(sum)