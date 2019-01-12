#https://open.kattis.com/problems/timeloop

magicnumber = int(
    input("Please provide a \"magic\" number between 1 and 100: "))
index = 1
for x in range(magicnumber):
    print(str(index) + " Abracadabra")
    index += 1
