#  Reverse a given number and return true if it is the same as the original number


def reverse_check(number):
    # number = int(input("Enter the number: "))  
    store_num = number
    revs_number = 0  

    while (number > 0):  
        remainder = number % 10  
        revs_number = (revs_number * 10) + remainder  
        number = number // 10  
      

    if store_num == revs_number:
        return True
    else:
        return False
    
print(reverse_check(1221))
