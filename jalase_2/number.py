import random
number = random.randint(1,100)
for i in range (10):
    a = int(input("number you:"))
    if(a>number):
        print("bya payin")
    elif(a<number):
        print("bro bala")
    else:
        print("you winner")
        print(i+1,"repetiton")
        exit()

print("you lost")