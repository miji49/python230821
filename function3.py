# function3.py

#가변 인자 처리
def union(*ar):
    result = []
    #HAM(0) | EGG(1)
    for item in ar:
        #H(0) | A(1) | M(2)
        for x in item:
            #만약에 x가 없다면
            if x not in result:
                result.append(x)
    return result

#함수를 호출
print(union("HAM","EGG"))
print(union("HAM","EGG","SPAM"))


#람다함수(이름이 없는 간단한 함수정의)
g = lambda x,y:x*y 
print(g(3,4))
print(g(5,6))
print((lambda x:x*x)(3))
print(globals())

print("---필터링함수---")
lst = [10,25,30]
iterL = filter(None, lst)
for item in iterL:
    print(item)

print("---람다함수정의---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)


#필터링하는 함수 정의
def getBiggerThan20(i):
    return i > 20

print("---일반함수정의---")
iterL = filter(getBiggerThan20, lst)
for item in iterL:
    print(item)

print("---람다함수정의---")
iterL = filter(lambda x:x>20, lst)
for item in iterL:
    print(item)