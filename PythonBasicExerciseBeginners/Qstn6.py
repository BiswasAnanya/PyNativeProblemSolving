#  Given a list of numbers, 
#  Iterate it and print only those numbers which are divisible of 5

given_list=[10,4,2,50,20,65,78,7,3]

for item in given_list:
    if item%5 == 0:
        print(item)