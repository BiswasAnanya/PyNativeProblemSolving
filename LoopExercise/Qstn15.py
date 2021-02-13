#  Use a loop to display elements from a given list which are present at even positions

my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
n= len(my_list)

for item in range(0,n,2):
    print(my_list[item])