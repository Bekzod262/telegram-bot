n = int(input("N sonini kiriting: "))

sanoq = 0

for i in range(1, n+1):
    if i%2 == 0:
        sanoq += i
print(sanoq)