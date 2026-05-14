print("Mini market, canclyator, mijoz qoshish, new tavarlarni qushish demak!")
balans = 1500
def Market():
    while True:
        print("Xush kelibsiz!")
        print("""
        1 --- Balans qoshish
        2 --- Balans ayirish
        3 --- Market historiy
        4 --- Balans uchirish
        5 --- Tavarlarni kurish
        0 --- boshqa dasturga utish demak!
        """) 

        tanlov = input("Tanlov qilloing hurmatli mijoz! ")

        if tanlov == "1":
            summa = int(input("Qancha summa qushmoqchisiz: "))
            balans += summa
            print("Mufaqatli qoshildi", balans)
        elif tanlov == "2":
            summa = int(input("Qancha summa ayirmoqchisiz: "))
            balans -= summa
            print("Mufaqatli ayirildi", balans)
        elif tanlov == "3":
            print("""
            Market historiy demak
            yangi narsalr kup and
            sikitgallar ham kup
            biz billan oxirgacha qolling!!!!!!
            """)
        elif tanlov == "4":
            summa = int(input("Qancha summa ayirmoqchisiz: "))
            balans -= summa
            print("Mufaqatli uchirildi", balans)
        
        elif tanlov == "5":
            savol1 = input("Tavarlarni kurasizmi? ha nad no>>>")
            if savol1 == "ha":
                savol2 = input("""Kepka, buruk , shaftoli, orik
                , ananas, nok, apelsin, 
                ollasizmi tanlang: """)
            else:
                print("Orqagaaaaaa???????")
        
        
        elif tanlov == "0":
            text()
            break

def text():
    while True:
        print("""
        xush kelibsiz::::::::
        1 --- qoshish
        2 --- kopaytirish
        3 --- Bolish
        4 --- ayirish
        5 --- oxirgi raqami
        0 --- Kengi dasturga utish demak !!!!!
        """)

        tanlov = input("Tanlov qiling hurmatli mijoz: ")

        if tanlov == "1":
            a = int(input("A son kiriting: "))
            b = int(input("B son kiriting: "))
            print(a+b)
        elif tanlov == "2":
            a = int(input("A son kiriting: "))
            b = int(input("B son kiriting: "))
            print(a*b)
        elif tanlov == "3":
            a = int(input("A son kiriting: "))
            b = int(input("B son kiriting: "))
            print(a/b)
        elif tanlov == "4":
            a = int(input("A son kiriting: "))
            b = int(input("B son kiriting: "))
            print(a-b)
        elif tanlov == "5":
            son = int(input("Son kiriting: "))
            print( son % 10)
        
        elif tanlov == "6":
            tbc()
            break

def tbc():
    balans = 1200
    while True:
        print("""
        TBC banka xush kelibsiz
        1 --- Bank xaqida malumot
        2 --- Bank kredit tarixi
        3 --- Bank aperatori billan boglanish
        4 --- Balans haqida kurish
        5 --- Bank ishga kirish
        0 --- Kengi dasturga utish: 
        """)

        tanlov = input("Tanlov qilling hurmatli mijoz: ")

        if tanlov == "1":
            print("""
            Bank haqida malumot 
            Bizning bankimiz juda yaxshi
            va barakali bankdir
            """)
        elif tanlov == "2":
            print("Sizning kredit tarixingiz yaxshi: ")
        
        elif tanlov == "3":
            print("Operatori 70 107 3005::::::")

        elif tanlov == "4":
            print("sizning balansingiz", {balans})
        
        elif tanlov == "5":
            print("Qachonki uz yunalishizi zuri bulling shunda demaK:")
        
        elif tanlov == "0":
            motivation()
            break

def motivation():
    savol1 = input("Ismingiz nimma: ")
    print(f"Tanishganimdan xursandman{savol1}")
    savol2 = input("Yoshingiz nechida|: ")
    print(f"Sizning yoshingz zur ekan {savol2}")
    savol3 = input("Sizni nimma qiynayapti: ")
    print(f""" Menimcha hamma narsaga imkon bor
    deb uyliyman Eng asosiysi Allohga tavakal
    qillish and oldinga harakat qillish and 
    kasbni yaxshisi bulish qulldan kelguncha {savol3}
    """)
    savol4 = input(f"Siz men boyman deb uylaysizmi: ")
    print(f"menimcha siz boysiz siz chunki sogsiz: ")
    print("""
    0 -- kengi dasturga utish: 
    """)
    tanlov = input("Tanlov kiriting: ")

    if tanlov == "0":
        next()
        break

def next():
    print("""
    Raqamlar bilan ishlayotgan bot:
    1 --- juft son topish
    2 --- Toq son topish
    3 --- 5 karali
    4 --- 6 karali
    5 --- 4 karali
    6 --- 3 karali
    0 --- Kengi dasturga utish
    """)

    tanlov = input("Tanlov qilling hurmatli mijoz: ")

    if tanlov == "1":
        son = int(input("son kiriting: "))
        if son % 2 == 0:
            print("juft son", son)
        else:
            print("Toq son", son)
    
    elif tanlov == "2":
        son = int(input("Son kiriting: "))
        if son % 2 != 0:
            print("Toq son", son)
        
        else:
            print("juft son", son)
    
    elif tanlov == "3":
        son = int(input("son kiriting: "))
        if  son % 5 == 0:
            print("It is right")
        else:
            print("It is not right: ")
    
    elif tanlov == "4":
        son = int(input("Son kiriting: "))
        if son % 6 == 0:
            print("It is right bekzod: ")
        else:
            print("It is not right bekzod: ")

    elif tanlov == "5":
        son = int(input("Son kiriting: "))
        if  son % 4 == 0:
            print("It is right: ")
        
        else:
            print("It is not right bekzod: ")
    elif tanlov == "6":
        son = int(input("Son kiriting: "))
        if tanlov % 3 == 0:
            print("it is right bekzod: ")
        else:
            print("Yes it is not right bekzod: ")
    elif tanlov == "0":
        game()
        break

def game():
    print("Lets start bekzod uyini boshladik: ")
    while True:
        print("""
        1 --- Bita son uylang: 
        2 --- Bita savat qushing:
        3 --- and undan narsani ayiring:
        4 --- Lets start bekzod: 
        0 --- Kengi dasturga utish: 
        """)

        tanlov = input("Tanlov qiling hurmatli mijoz: ")

        if tanlov == "1":
            print("It is right: ")
        
        if tanlov == "2":
            print("Lets satart bekzod: ")
        
        if tanlov == "3":
            print("Yes of course: ")
        
        if tanlov == "4":
            print("It is very good: ")
        
        if tanlov == "0":
            max()
            break

def max():
    print("KATTASINI TOPUVCHI DASTUR: ")
    while True:
        print("""
        1 --- Sonlarni katasini topuvcjhi bot
        0 --- kengi dasturga utkazish: 
        """)
        tanlov = (input("Tanlov qilling hurmatli mijoz: "))

        if tanlov == "1":
            a = int(input("son kiriting: "))
            b = int(input("son kiriting: "))
            c = int(input("son kiriting: "))
            if a > b and a > c:
                print("Eng katasi ", a)
            elif b > a and b > c:
                print("Eng kattasi ", b)
            else:
                print("eng katasi", c)
        elif tanlov == "0":
            break
Market()