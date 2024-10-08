a = (list(input("enter your number with spaces:").split()))


def tamrin10(d):
        for d in d:
            if int(d) % 2 == 0:
                return d
result = filter(tamrin10,a)
print(list(result))