multiple35 = []


for x in range(0,1000):
    if x % 3 == 0 or x % 5 == 0:
        multiple35.append(x)

print(sum(multiple35))