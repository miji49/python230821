# DemoFormat.py
for x in range(1,6):
    print(x,"*",x,"=",x*x)

print("---오른쪽 정렬---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).rjust(3))

print("---0으로 채우기---")
for x in range(1,6):
    print(x,"*",x,"=",str(x*x).zfill(5))


#문자열 결합
#url = "http://www.multicampus.com/?page=" + 1
#print(url)
url = "http://www.multicampus.com/?page=" + str(1)
print(url)

for i in range(10):
    url = "http://www.multicampus.com/?page=" + str(i)
    print(url)


#파일쓰기
f = open("c:\\work\\demo.txt", "wt", encoding="utf-8")
f.write("첫번째\n두번째\n세번째\n")
f.close

#파일읽기(raw string notation)
f = open(r"c:\work\demo.txt", "rt", encoding="utf-8")
result = f.read()
print(result)

f.close()


#서식지정
print("{0:x}".format(10))
print("{0:b}".format(10))
print("{0:e}".format(4/3))
print("{0:f}".format(4/3))
print("{0:.2f}".format(4/3)) #소숫점
print("{0:,}".format(15000000)) #화폐

