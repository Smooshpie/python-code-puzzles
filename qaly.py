#https://open.kattis.com/problems/yoda
def calc(a, b, outa, outb, ctra, ctrb, depth):
    moda = int(a % 10)
    modb = int(b % 10)

    if a == 0 and b == 0:
        print("YODA") if ctra == 0 else print(outa)
        print("YODA") if ctrb == 0 else print(outb)
        return

    if(moda > modb):
        outa += moda * 10**ctra
        ctra += 1
    else:
        outb += modb * 10**ctrb
        ctrb += 1

    calc(int(a / 10), int(b / 10), outa, outb, ctra, ctrb, depth + 1)


a = int(input("Number1: "))
b = int(input("Number2: "))

calc(a, b, 0, 0, 0, 0, 0)