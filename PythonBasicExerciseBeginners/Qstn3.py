# Given a string, display only those characters which are present at an even index number.

given_string=input()
n= len(given_string)
# print(n)

for i in range (0,n):
    if i%2 == 0:
        print(given_string[i])