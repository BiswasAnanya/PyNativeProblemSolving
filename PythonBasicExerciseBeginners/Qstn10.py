# Given a two list of numbers create a new list such that 
# new list should contain only odd numbers from
# the first list and even numbers from the second list

First_List =[10, 20, 23, 11, 17]
Second_List =[13, 43, 24, 36, 12]
def mergelist(First_List,Second_List):

    new_list=[]

    for item in First_List:
        if item%2 != 0:
            new_list.append(item)
    for item in Second_List:
        if item%2 == 0:
            new_list.append(item)
    return new_list


print(mergelist(First_List,Second_List))