
a = int(input("Enter the number tuples: "))
tuples = []
for i in range (a):
            b= input(f"{i+1}tuple seperated by a space (a b): ")
            s , y = map(int, b.split())
            tuples.append((s, y))
c = sorted(tuples, key=lambda x: x [1])
print(c)
