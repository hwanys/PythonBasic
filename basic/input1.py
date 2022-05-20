# 입력 : input()

# msg = input()
# print(msg)

# msg = input("이름입력 : ")
# print(msg)

# num1 = input("Num1 : ") # str 타입 입력
# num2 = input("Num2 : ") 
# print(num1 + num2)  # 문자 연결 출력

# num1 = int(input("Num1 : ")) # int 타입 입력
# num2 = int(input("Num2 : ")) 
# print(num1 + num2)  # int 연산 가능

# 실습
# 년/월/일 형태로 입력 받은 후 10년 후 날짜를 출력하기
# 2022/05/20 => 2032년 05월 20일

# 내 코드
date = input("날짜입력(년/월/일)")
date = date.split("/")
print("입력한 날짜의 10년 후는 ? %s" % (str(int(date[0])+10)+"년 "+date[1]+"월 "+date[2]+"일") )

# 수업 코드
date1 = input("날짜입력(년/월/일)")
pos = date1.find("/")
year = int(date1[:pos]) + 10
print("입력한 날짜의 10년 후는 ? %s" % (str(year)+"년 "+date1[5:7]+"월 "+date1[8:]+"일") )



