# Given a range of first 10 numbers, Iterate from start number to the end number and 
# print the sum of the current number and previous number

n=10
prev_num=0
for item in range(0,n):
    current_num = item
    sum = current_num+prev_num
    print("Current Number:",current_num,end=" ")
    print("Previous Number:",prev_num,end=" ")
    print("Sum",sum)
    prev_num = current_num

