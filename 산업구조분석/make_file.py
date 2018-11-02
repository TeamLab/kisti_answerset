

with open("./list.txt", "r") as f:
    codes = [code.strip() for code in f.readlines()]
for code in codes:
    with open("산업구조분석_"+code +".md", "w", encoding="utf8") as f:
        f.write("## 산업구조분석이란?")
