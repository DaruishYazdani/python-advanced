import csv
file = input("enter file:")
with open (file, "r" , encoding="utf_8") as expense :
    head = csv.reader(expense)
    headers = next(head)
    print(headers)
    for i in head :
        print(i)
