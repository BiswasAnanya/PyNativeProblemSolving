# Display the cube of the number up to a given integer

given_number= int(input())
result= 1

if given_number != 0:
        result=given_number*given_number*given_number
else:
    print("0")
print(result)
