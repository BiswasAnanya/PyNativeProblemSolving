# Write a code to extract each digit from an integer, in the reverse order

def reverse_check(number):
    # number = int(input("Enter the number: "))  
    store_num = number
    revs_number = 0  

    while (number > 0):  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10 

    return revs_number
    
print(reverse_check(1234))
