#전역변수
str = "Not Class Member"
class GString:
    def __init__(self):
        #인스턴스 멤버 변수
        self.str = "" 
    def set(self, msg):
        self.str = msg
    def print(self):
        #버그(모호한 것보다는 명시적인 것이 좋다!, str이 아닌 self.str)
        print(self.str)

g = GString()
g.set("First Message")
g.print()