sanoq = 0

son = int(input("Son kiriting: "))

while son != 0:
    if son < 0:
        sanoq  += 1
    son = int(input("Son kiriting: "))

print(sanoq)