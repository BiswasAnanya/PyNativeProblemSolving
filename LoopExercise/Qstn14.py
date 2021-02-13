# Reverse a given integer number. 
# Given:
# 76542

given_number= 76542
revs_number=0

while given_number>0:
    remainder= given_number%10
    revs_number= (revs_number*10)+remainder
    given_number=given_number//10
print(revs_number)