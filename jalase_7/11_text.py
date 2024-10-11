a = input("enter book:")

with open(a,"r" , encoding= "utf-8") as file :
    b = file.read()

def book (words):
    word = 0
    say_the_word = words.split()
    for i in say_the_word:
        word =+ 1
        return word
def books (search,word):
    words = 0
    say_the_word = search.split()
    for j in word:
        say_the_word =words.count(word)
        return say_the_word
search_word = input("kalame morede nazar ra vared konid : ")
say_the_word = search_word.split()
with open("report.text", "w", encoding="utf-8") as report:
    report.write(f"The count of the word you gave me: {search_word}""\n")
    report.write(f"The count of all words: {say_the_word}""\n")
with open("report.txt", "r", encoding='utf-8') as reportt:
    print(reportt.read())
