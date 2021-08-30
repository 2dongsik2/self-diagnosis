import hcskr, json

file = open('info.json', encoding='UTF8')
jsonString = json.load(file)
for user in jsonString:
    res = hcskr.selfcheck(*user)
    print(res)