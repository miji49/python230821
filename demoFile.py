# demoFile.py

f = open("c:\\work\\demo2.txt", "wt", encoding="utf-8")
f.write("데이터1번\n데이터2번\n데이터3번\n")
f.close

#읽기
f = open("c:\\work\\demo2.txt", encoding="utf-8")
result = f.read()
print(result)
print("---readline()----")
f.seek(0)
print(f.readline(), end="")
print(f.readline(), end="")
print("---readline()----")
f.seek(0)
lst = f.readlines()
for item in lst:
    print(item, end="")
f.close()

