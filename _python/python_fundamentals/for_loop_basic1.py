# 1

for num in range(0, 151, 1):
    print(num)

#2

for num in range(5, 1001, 5):
    print(num)

#3

for num in range (1, 101, 1):
    if num % 10 == 0:
        print("Coding Dojo")
    elif num % 5 == 0:
        print("Coding")
    else:
        print(num)

#4

count = 0
for num in range(0, 500001, 1):
    if num % 2 != 0:
        count += num

print(count)

#5

for num in range(2018, -1, -4):
    print(num)

#6

lowNum = 1
highNum = 11
mult = 2

for num in range(lowNum, highNum, 1):
    if num % 2 == 0:
        print(num)