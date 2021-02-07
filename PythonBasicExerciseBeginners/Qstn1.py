# Given a two integer numbers return their product and  
# if the product is greater than 1000, then return their sum

def multiplication_or_sum(num1, num2):
    product = num1*num2
    if product <= 1000 :
        return product
    else:
        sum =num1 +num2
        return sum
    
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# result = multiplication_or_sum(num1,num2)
# print(result)


result = multiplication_or_sum(20,30)
print(result)