# Print the following pattern
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# *
n=6
space=" "
for item in range(1,n):
    print(item*"* ")
for item in range(n-1,0,-1):
    print(item*"* ")