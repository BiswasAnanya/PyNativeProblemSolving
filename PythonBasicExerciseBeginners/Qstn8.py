# Print the following pattern
# 1 
# 2 2 
# 3 3 3 
# 4 4 4 4 
# 5 5 5 5 5

n=5
for item in range(1,n+1):
    for i in range(item):
        print(item,end=" ")
    print("\n")