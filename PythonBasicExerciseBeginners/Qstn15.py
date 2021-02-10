# Write a function called exponent(base, exp) that 
# returns an int value of base raises to the power of exp.

base= int(input("Base: "))
exponent= int(input("Exponent: "))
result =1 

while exponent>0:
    result=base*result
    exponent -= 1
print("The result is:",result)