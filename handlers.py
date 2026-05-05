min = None

while True:
    text = input("Sen kiriting (stop chiqish):")

    if  text == "stop":
        break
    n = int(text)

    if min  is None:
        min = n
    elif n <  min :
        min = n
print("Eng kichik son: ", min)
