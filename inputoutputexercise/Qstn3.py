#Convert decimal number to octal using print() output formatting

# dec= int(input("Give a decimal number: "))
val = 256
quoteint=1
new_string=""

while quoteint != 0:
    remainder = val%8   # 0
    quoteint = val//8    # 2
    print(remainder)
    new_string=new_string+str(remainder)
    val=quoteint   # 2
print(int(new_string))
# number = int(new_string)
# print(number,end='')

# revs_number = 0  

# while (number > 0):  
#     remainder1 = number % 10  
#     revs_number = (revs_number * 10) + remainder1  
#     number = number // 10  
# print(revs_number)
# print (oct(dec), "in octal")

