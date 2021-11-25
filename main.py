def decode(txt,key):
    otp = ""
    for obj in txt:
        if obj.isalpha():
            isupper = obj.isupper()
            obj = obj.lower()
            kod = ord(obj)
            kod -= key
            if kod < 97:
                kod += 26
            if isupper:
                otp += chr(kod).upper()
            else:
                otp += chr(kod)
        else:
            otp += obj
    return otp

def encode(txt,key):
    otp = ""
    for obj in txt:
        if obj.isalpha():
            isupper = obj.isupper()
            obj = obj.lower()
            kod = ord(obj)
            kod += key
            if kod > 112:
                kod -= 26
            if isupper:
                otp += chr(kod).upper()
            else:
                otp += chr(kod)
        else:
            otp += obj
    return otp

def main():
    while True:
        print("Wybierz tryb:","Dla Szyfrowania wpisz E","Dla deszyfrowania wpisz D",sep="\n")
        mode = input()
        if mode == "E":
            print("Moduł Szyfrowania\nAby Opuścić wpisz frazę EXIT")
            while True:
                print("Podaj text")
                txt = input()
                if txt=="EXIT":
                    break;
                print("Podaj klucz")
                key=input()
                print("Szyfr "+txt+" z kluczem "+key+" to:")
                print(encode(txt,int(key)))
        elif mode == "D":
            print("Moduł Deszyfrowania")
            while True:
                print("Podaj text")
                txt = input()
                if txt=="EXIT":
                    break;
                print("Podaj klucz")
                key=input()
                print("Deszyfr "+txt+" z kluczem "+key+" to:")
                print(decode(txt,int(key)))
        else:
            print("nierozponano modułu")
main()