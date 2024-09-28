number = int(input("NUMBER: "))
 
def paskal(n):
    multi = 1
    for i in range(n,0,-1):
        multi*=i
    return multi
def khayam (number):
    for n in range(number):
        subList = []
        for k in range(n+1):
            item = paskal(n)//(paskal(k)*paskal(n-k))
            subList.append(item)
        print(subList)
 
khayam(number)

