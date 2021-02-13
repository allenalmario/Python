# Using Python, 

# [x] print all the numbers from 0 to 10
for num in range(0, 11):
    print(num)
# [x] print all the odd numbers from 0 to 3000
for num in range(0, 3001):
    if num % 2 != 0:
        print(num)
# [x] create a function that iterates through each 
#     value in the list and print out each value
def eachValue(l):
    for itm in l:
        print(itm)
    
eachValue([1,2,3,4,5])
# [x] create a function that takes a list as an 
#     argument and returns a sum of all of its values

def total(l):
    count = 0
    for num in range(0, len(l)):
        count = count + l[num]
    return count

totalValue = total([10, 11, 12, 13, 14])
print(totalValue)