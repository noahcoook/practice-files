import  re



with open(r"C:\Users\Noah\source\repos\practice-files\python\regexData.txt", "r", encoding="utf-8") as f:
    data = f.read()

pattern = re.compile(r'/d{1,10}')

matches = pattern.finditer(data)


#print(matches)


#matches.group(0)


for match in matches:
    print(match)

