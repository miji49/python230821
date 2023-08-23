# db1.py

import sqlite3

#일단 메모리에 저장
#con = sqlite3.connect(":memory:")

#파일에 저장
con = sqlite3.connect("c:\\work\\sample.db")

#구문 실행은 커서 객체에서
cur = con.cursor()
#테이블 구조 생성(ANSI SQL 92, 99에서 표준)
cur.execute("create table if not exists PhoneBook " + " ( id integer primary key autoincrement, name text, phoneNum text);")

#1건 입력
cur.execute("insert into PhoneBook (name, phoneNum) values ('홍길동', '010-111');")

#입력 파라메터 처리
name = "전우치"
phoneNumber = "010-222"
cur.execute("insert into PhoneBook (name, phoneNum) values (?, ?);", (name, phoneNumber))

#다중의 레코드 입력
datalist = (("박문수","010-123"), ("김길동","010-456"))
cur.executemany("insert into PhoneBook (name, phoneNum) values (?, ?);", datalist)

#결과 확인
cur.execute("select * from PhoneBooK;")

print(cur.fetchall())


#커밋을 실행
con.commit()

#연결닫기
con.close()
