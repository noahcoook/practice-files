import  re



with open(r"./python/regexData.txt", "r", encoding="utf-8") as f:
    data = f.read()

pattern = re.compile(r'[A-Za-z0-9+._-]+@')

matches = pattern.finditer(data)


#print(matches)


#matches.group(0)


for match in matches:
    print(match)

