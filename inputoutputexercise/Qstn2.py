#Display “My Name Is James” as “My**Name**Is**James” using output formatting of a print() function

given_string= "My Name is James"
print(given_string.split())


splitted_result = given_string.split()
print(type(splitted_result))
print( splitted_result[0], splitted_result[1], splitted_result[2], splitted_result[3], sep= '**' )
# print( *splitted_result, sep= '**' )

# for item in splitted_result :
#     print(item + "**", end ="")

n= len(splitted_result)        
for i in range(0,n-1):
    print(splitted_result[i]+'**',end="")
for i in range(n-1,n):
    print(splitted_result[i])

# print(splitted_result[-1])


# print('My', 'Name', 'is', 'James', sep='**')

