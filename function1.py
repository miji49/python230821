# function1.py
#함수 정의
def setValue(newValue):
    #지역변수
    x = newValue
    print("지역변수 x:", x)

#함수 호출
result = setValue(5)
print(result)

#여러개 값을 리턴
def swap(x,y):
    return y,x

#호출
print(swap(3,4))