book = input("lotfan fail ra vared konid:")
with open (book,"r",encoding="utf_8") as file:
    count = file.read()
p = (len(count))
def kh (khat):
    count = 0
    for i in khat:
       if i == " ":
            count = count+1
word = input("kalame mored nazar :")
massage = book
v = (massage.find(word))
with open ("report.text","w",encoding="utf_8") as report:
    report.write("/n"f"tedat kalamat hast : {p}""/n")
    report.write(f"tedad khat ha hast: {count}""/n")
    report.write(f"tedad kalame mored nazar : {v}""/n")
with open ("report.text","r",encoding="utf_8") as report:
    report=report.read()
    print(report)
with open ("report.text","w",encoding="utf_8") as report:
    report.write(" ")