# Given a list iterate it and display numbers 
# which are divisible by 5 and if you find number greater than 150 stop the loop iteration

list1 = [12, 15, 32, 42, 155, 75, 122, 132, 150, 180, 200]

for item in list1:
    if (item%5) == 0:
        if item <= 150:
            print(item)
        else:
            break

