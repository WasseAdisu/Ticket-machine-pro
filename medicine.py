from drug_store import darug_store
from Time import  *


def message(reminder):
    return reminder


reminder = message("Please wait until the seller calls you.")

print("Well come to our Drug store")
list = [123456789, 987654321]
count = 0
count_limit = 3
while count_limit > count:
    id = int(input("please enter your id: "))
    if id in list:
        order = input("please choose products name above : ")
        while order != "":
            darug_store()
            per = input("Do you want continue? y/n: ")
            if per == "y":
                order = input("please choose products name above: ")
            else:
                exit(0)
            count += 1

        else:
            print("Try after a minute")
