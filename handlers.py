print ("MINI KALKYATOR<<<<<")
print("YOU ARE WELKOME ????????")
while True:
    print("""
    1 --- Kopaytirish
    2 --- Bollish
    3 --- Ayirish
    4 --- qoshish
    5 --- chiqib ketish
    6 --- foiz hisoblash
    7 --- oxirgi raqamni topish
    8 --- raqamlarni qoshish
    9 --- bush savatda raqam and son qushish
    10 --- bush savatda and yangi narsallar qushish
    11 --- Login and parol yaratish
    12 --- listdan xoxlagan son chiqarish
    13--- Motivation gaplar///////>>>>>
    """)
    tanlov = input("Tanlov Hurmatli mijoz: ")
    if tanlov == "1":
        a = int(input("son kiriting: "))
        b = int(input("son kiriting: "))
        print(a*b)
        print("MUFAQATLI BOLDI>>>>/")
    elif tanlov == "2":
        a = int(input("Son kiriting: "))
        b = int(input("Son kiriting: "))
        print(a/b)
        print("MUFAQATLI BOLLINDI///")
    elif tanlov == "3":
        a = int(input("Son kiriting: "))
        b = int(input("Son kiriting: "))
        print(a - b)
        print("Mufaqatli Bolldi")
    elif tanlov == "4":
        a = int(input("son kiriting: "))
        b = int(input("son kiriting: "))
        print(a + b)
        print("Mufaqatli qoshildi")
    elif tanlov == "5":
        son = input("son kiriting: ")
        if son == 0:
            print("Dastur tugadi/")
            break
    elif tanlov == "6":
        son = 100
        foiz = 20
        javob = son * foiz / 100
        print(javob)
    elif tanlov == "7":
        son =int( input("Son kiriting: "))
        print(son % 10)
        print("Mufaqatli bolldi demak bekzod")
    elif tanlov == "8":
        son = int(input("Son kiriting: "))
        yigindi = 0
        while son > 0:
            oxirgi = son % 10
            yigindi += oxirgi
            son = son // 10
        print("Yigindi", yigindi)
    elif tanlov == "9":
        savat = []

        for i in range(6):
            son = input("son kiriting: ")
            savat.append(son)
            print(savat)
            print("Mufaqatli bolldi jigar////")
    elif tanlov == "10":
        mevalar = ["ollma", "nok", "shaftoli", "banan"]
        mevalar.append("uzum")
        mevalar.append(1)
        mevalar.append(2)
        mevalar.append(3)
        mevalar.append(4)
        mevalar.append(5)
        mevalar.append(6)
        print(mevalar)
    elif tanlov == "11":
        login = "admin"
        parol = "1234_bekzod"
        while True:
            user = input("Login kiriting: ")
            kod = input("parol kiriting:  ")
            if user == login and kod == parol:
                print("Yo are welkome: ")
                break
            else:
                print("Enter again please broooo>>>>")
    elif tanlov == "12":
        son = [1,2,3,4,5,5,6,7]
        print(son[0])
        print(son[1])
        print(son[-1])
        print(son[2])
        print(son[3])
    elif tanlov == "13":
        print("""
        1__SEN UZINGA ISHON
        2__HECH KIM ISHONMAGANDA HAM SEN UZINGA ISHON
        HECH KIMNI GAPI QIZIQ BULLMASIN HAMA NARSANI 
        VAQTI BOR VA HAMMANI UZINI VAQTI BOR DEMAK
        SEN USHA VAQTNI KUT AND XARAKT QILL BEKZOD
        3_____TERNEROFKANI QATIQ QILL VA OGIR ISHLA
        QULDAN KELGUNCHA OQSIL YEGIN BEKZOD DEMAK 
        SENGA HECH KIM ISHONMAGANDA SEN UZINGA ISHON )
        AND ALLOHGA ISHON BEKZOD LETS START BEKZOD"""
        )
        