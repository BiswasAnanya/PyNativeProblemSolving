# Given a string and an integer number n, 
# remove characters from a string starting 
# from zero up to n and return a new string

given_string= "WelcometoPYnative"
n=5
length=len(given_string)
new_string=""

for item in range(n, length):
    char=given_string[item]
    new_string=new_string+ char
print(new_string)