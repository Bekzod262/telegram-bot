print("Assalomu alleykum xush kelibsiz: ")
balans = 1500
while True:
    print("""
    Tbc bank you are welkome
    1---Royxatdan utish
    2---malumot ollish
    3---Aperaterga telfon qilish
    4---summa qushish
    5---summa ayirish
    6---chiqish demak
    7---boshiga qaytish demak
    8---Tbc tarixi demak
    9---kredit qancha ollish demak
    10---I will try again""")

    tanlov = input("Tanlov : ")
    if tanlov == "1":
        bekzod = input("Son kiriting: ")
        if bekzod != 0:
            print("Davom etamiz demak bekzod:>>>")
        else:
            print("Buldi tugatamiz demak:>>>>>>>>>>")
        print("""Ruyxatdan utish demak birinchi numer
        kiratiz and va saqlab kirasiz demak""")
    elif tanlov == "2":
        print("""Malumot turlari demak
        2 xill bulladi tanlaysiz jigarillo""")
    elif tanlov == "3":
        print(""" Aperatirga Boglanish demak
        tugri anig ullab beramiz jigar""")
    elif tanlov == "4":
        summa  = int(input("Qancha balans qushishni xoxlaysiz"))
        balans += summa
        print(f"Balans { balans} uzgardi demak:>>")
    elif tanlov == "5":
        summa = int(input("Qancha balansni ayirishni xoxlaysiz"))
        balans -= summa
        print(f"Mufaqatli {balans} ayirildi demak:")
    elif tanlov == "6":
        print("chiqsh demak 6 bosing and chiq\di va qaytadi")
    
    elif tanlov == "7":
        print("Boshiga qaytish demak bekzod:>>>")

    elif tanlov == "8":
        print("Tbc tarixi demak bekzod:>>>>")
    
    elif tanlov == "9":
        print("Krdit 5milliondan 100milongacha ollish mumkin>>>")
    elif tanlov == "10":
        print("I will try agin do you understand bekzod>>>>>>>>>")
        break
    
    else:
        print("dastur tugadi demak:")
        print("lets gooo bekzod Start bekzod")

