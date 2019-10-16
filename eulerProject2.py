x1 = 1
x2 = 2
x3 = 3

numbers = [1]

while x1 < 4000000 or x2 < 4000000 or x3 < 4000000:
    x3 = x1 + x2 # x = 1 + 2
    x1 = x2 # x1 = 2
    x2 = x3 #x2 = 3
    numbers.append(x1)
    print(x1, x2, x3)

print(numbers)

sumnumbers = []

for number in numbers:
    if number % 2 == 0:
        sumnumbers.append(number)
    
print(sum(sumnumbers))