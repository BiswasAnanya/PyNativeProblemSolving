# Display float number with 2 decimal places using print()

float_num = 23.45696565
# print( '%.2f' %23.45696565 )

num_string = str(float_num)
num_list= []

for item in num_string:
    num_list.append(item)

index= num_list.index('.')

new_list= num_list[0:index+3]
print(new_list)
# for item in new_list:
#     print(item, end='')
new_string= ""
for item in new_list:
    new_string = new_string+item

new_float_num= float(new_string)
print(new_float_num)



# list('Hello')  # ['H', 'e', 'l', 'l', 'o']
# def list_(string) -> list

# join_(['H', 'e', 'l', 'l', 'o'])  # 'Hello'
# def join_(list(str)) -> string

# join_('**', ['H', 'e', 'l', 'l', 'o'])  # 'H**e**l**l**o'
# def join_(str, list(str)) -> string