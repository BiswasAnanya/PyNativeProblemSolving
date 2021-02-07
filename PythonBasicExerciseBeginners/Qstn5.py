# Given a list of numbers, return True if first and last number of a list is same

given_list= [1,2,3,4,5,6,1,2,1]
given_list1 = [3,5,3,5,1,12,4]

length= len(given_list1)
# print(length)
def check():
    if given_list1[0]== given_list1[length-1]:
        return True
    else:
        return False
check()
print(check())