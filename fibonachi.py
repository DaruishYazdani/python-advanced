n = int(input("how many? "))
fibo_list = []
for i in range(n):
    if i == 0 or i == 1:
        fibo_list.append(1)
    else:
        fibo_list.append(fibo_list[i-1] + fibo_list[i-2])
print(fibo_list)