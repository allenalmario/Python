import random
def randInt(min="0", max="100"):
    num = random.random() * (float(max) / float(2)) + float(min)
    return int(round(num))
print(randInt())
print(randInt(max=50))
print(randInt(min=50))
print(randInt(min=50, max=500))
