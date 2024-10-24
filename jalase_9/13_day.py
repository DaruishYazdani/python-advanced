import xml.etree.ElementTree as ab
file = input("enter file:")
note = ab.parse(file)
root = note.getroot()
for book in root.findall("Task") :
    print(book.find("Title").text)
    print(book.find("DueDate").text)
    print(book.find("Priority").text)
    print(book.find("Status").text)
    print(10 * "#*")