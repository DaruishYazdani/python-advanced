x = lambda a : a*a
my_list = []
num = int(input("how many numbers do you have?"))
for i in range(num):
    item = int(input("enter you number :"))
    my_list.append(item * item)
print(my_list)