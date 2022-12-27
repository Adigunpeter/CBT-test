

# sample
info = []
def reg():
    fullname = input("Enter your name here>>")
    pin = input("Enter your Pin here>>")
    myinfo = [fullname, pin]
    info.append(myinfo)
    print(info)


def login():
    reg()
    myfullname = input("Enter your name here to login>>")
    mypin = input("Enter your Pin here to login>>")
    print(info[0])
    if myfullname == info[0][0] and mypin == info[0][1]:
        print("login successful")
    else:
        print("can't login")

login()
