#Python program to display all the prime numbers within a range

def search_prime(given_number):

    if given_number>1:
        for item in range(2,given_number-1):
            if (given_number%item) == 0:
                print("Not prime")
                break
        else:
            print("Prime")
            

    else:
        print("1 is not prime number.")    

    return


given_number= int(input("Enter number: "))
search_prime(given_number)



# 7
# 7%2==0, prime
# 7%3==0
# 7%4==0
# 7%5==0
# 7%6==0
# 7 is prime - correct

# 6
# 6%2==0, Not prime
# 6%3==0 x
# 6%4==0 x
# 6%5==0 x