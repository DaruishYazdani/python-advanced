import json
file = input("enter file:")
with open (file ,  encoding="utf_8") as file_json:
    files = json.load(file_json)
nume = {"sector", "fullTimeEmployees", 
"longBusinessSummary", "city", "country", "phone"
}
for i in nume:
    for j in files:
          if i == j:
            print(f"{i}: {files[j]}\n")
