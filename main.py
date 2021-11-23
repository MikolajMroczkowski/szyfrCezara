def decode(txt,key):
    otp = ""
    for obj in txt:
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
    return otp

def encode(txt,key):
    otp = ""
    for obj in txt:
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
    return otp
str="AZ"
print(encode(str,3),decode(encode(str,3),3),sep=";")