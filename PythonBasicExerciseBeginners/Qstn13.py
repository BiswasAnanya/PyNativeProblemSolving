#Print multiplication table form 1 to 10

n =10
for item in range (1,n+1):
    for i in range(1,n+1):
        print(item*i,end =" ")
    print("\n")