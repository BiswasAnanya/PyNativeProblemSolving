# Calculate income tax for the given income by adhering to the below rules

# Taxable Income	Rate (%)
# First $10,000	0
# Next $10,000	10
# The remaining	20

income =45000
if income >= 20000:
   first_taxpayable = 10000*(0/100)
   second_taxpayable = 10000*(10/100)
   remain_taxpayable = (income-20000)*(20/100)
total_taxpayable = first_taxpayable + second_taxpayable + remain_taxpayable
print(total_taxpayable)
