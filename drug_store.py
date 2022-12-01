from medicine import *

cosmotics = 0
medecine = 0
perfume = 0
print("cosmetics")
print("perfume")
print("medicine")


def darug_store():
    order = input("please choose products name above : ")
    if order == "cosmotics":
        global cosmotics
        cosmotics = cosmotics + 1
        print("Your number is : c-", cosmotics)
    elif order == "perfume":
        global perfume
        perfume = perfume + 1
        print("Your number is: p -", perfume)
    elif order == "medicine":
        global medecine
        medecine = medecine + 1
        print("Your number is: m -", medecine)
