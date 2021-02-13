# 1

def big(l):
    for x in range(0, len(l)):
        if l[x] > 0:
            l[x] = "big"
    return l

biggie = big([-1, 2, -3, 4, -5, 6])
print(biggie)

#2

def countPositives(l):
    posCount = 0
    for x in l:
        if x > 0:
            posCount += 1
    return posCount

x = countPositives([-1, 1, 1, 1])
print(x)

#3

def sum(l):
    sum = 0
    for x in l:
        sum = sum + x
    return sum

total = sum([1,2,3,4,5])
print(total)

#4

def average(l):
    sum = 0
    for x in l:
        sum = sum + x
    avg = float(sum) / len(l)
    return avg

mean = average([1,2,3,4])
print(mean)

#5

def length(l):
    count = 0
    for x in l:
        count = count + 1
    return count

count = length([101,296,365,900,67])
print(count)

#6

def minimum(l):
    if (len(l) <= 0):
        return False
    min = 0
    for x in l:
        if x < min:
            min = x
    return min

print(minimum([37, 2,1,-9]))
print(minimum([]))

#7

def maximum(l):
    if (len(l) <= 0):
        return False
    max = 0
    for x in l:
        if x > max:
            max = x
    return max

print(maximum([37, 2,1,-9]))
print(maximum([]))

#8

def ultimate_analysis(l):
    sumTotal = 0
    min = 0
    max = 0
    length = 0
    for x in l:
        if x > max:
            max = x
        if x < min:
            min = x
        length = length + 1
        sumTotal = sumTotal + x
    avg = float(sumTotal) / length
    info = {'sumTotal': sumTotal, 'average': avg, 'minimum': min, 'maximum': max, 'length': length}
    return info

print(ultimate_analysis([37,2,1,-9]))

#9

def reverse_list(l):
    counter = 0
    for x in range((len(l) - 1), (len(l) - 1) / 2, -1):
        temp = l[x]
        l[x] = l[0 + counter]
        l[0 + counter] = temp
        counter += 1
    print(l)

reverse_list([37, 2, 1, -9])

# def reverse_list(l):
#     for x in range(0, len(l) / 2):
#         temp = l[0 + x]
#         l[x] = l[(len(l) - 1) - x]
#         l[(len(l) - 1) - x] = temp
#         print(l)

# reverse_list([37, 2, 1, -9, 5, 6, 7])