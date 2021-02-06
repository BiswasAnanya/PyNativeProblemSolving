# Determine if given number is Pelindromic or not
# input:
# 1221
# output:
# YES

number = int(input("Enter the number: "))  
store_num = number
revs_number = 0  

while (number > 0):  
    remainder = number % 10  
    revs_number = (revs_number * 10) + remainder  
    number = number // 10  
print(revs_number)  

if store_num == revs_number:
    print("Yes")
else:
    print('No')

