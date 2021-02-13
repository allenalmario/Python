# 1

def countdown(num):
    numbers = []
    for x in range(num, -1, -1):
        numbers.append(x)
    return numbers

numbers = countdown(5)
print(numbers)

# 2

def print_and_return(x):
    for num in x:
        print(num)

print_and_return([1,2])

# 3

def first_plus_length(x):
    return(x[0] + len(x))

print(first_plus_length([1,2,3,4,5]))

#4

def values_greater_than_second(l):
    if len(l) < 2:
        return false
    new_list = []
    count = 0
    for num in l:
        if num > l[1]:
            count += 1
            new_list.append(num)
    print(count)
    return new_list

new_list = values_greater_than_second([5,2,3,2,1,4])
print(new_list)

# 5

def length_and_value(x, y):
    repeat = []
    for z in range(0, x):
        repeat.append(y)
    return repeat

print(length_and_value(6,2))