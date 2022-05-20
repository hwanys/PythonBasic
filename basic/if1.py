# 파이썬 {} 사용하지 않음/ 들여쓰기 사용함
# if 
# if True:
#     print("True")

a = 200
# if a < 100:
#     print("a는 100보다 작다")
# print("조건문에서 들여쓰기는 중요함")

# a는 100과 200사이에 있다
# if a >= 100 and a <= 200:
#     print("a는 100과 200사이에 있다")


# if 100 <= a <= 200:
#     print("a는 100과 200사이에 있다")

# 실습
a, b, c = 12, 6, 18

# 가장 큰 수 출력하기

# 내가 한 노가다 코드
# if a < b:
#     if b < c:
#         print("가장 큰 수는 %d" % c)
#     else:
#         print("가장 큰 수는 %d" % b)
# else:
#     if a < c:
#         print("가장 큰 수는 %d" % c)
#     else:
#         print("가장 큰 수는 %d" % a)

# 쉅
# max = a
# if max < b:
#     max = b
# if max < c:
#     max = c

# print("제일 큰 수",max)


# if~else

# if True:
#     print("True")
# else:
#     print("False")

# a = 55
# if a < 100:
#     print("a는 100보다 작다")
# else:
#     print("a는 100보다 크다")

# print()
# score,grade = 90,"A"
# if score >= 90 and grade == "A":
#     print("합격")
# else:
#     print("불합격")

# # 실습 - 숫자를 입력받은 후 짝/홀 출력
# num = int(input("숫자를 입력하세요 "))
# if num % 2 == 0:
#     print("%d는 짝수 입니다" % num)
# else:
#     print("%d는 홀수 입니다" % num)

print()


# import datetime

# now = datetime.datetime.now()
# print(now)  # 2022-05-20 15:13:25.483375
# print("{}년 {}월 {}일 {}시 {}분 {}초".format(now.year,now.month,now.day,now.hour,now.minute,now.second))

# if now.hour < 12:
#     print("오전")
# else:
#     print("오후")

# print("오전" if now.hour < 12 else "오후")


# # 삼항 연산자   -> "참일때 출력문" if 조건 else "거짓일때 출력문"
# str = "안녕하세요" if True else "반갑습니다."
# print(str)

# 중첩 if
a = 75
if a > 50:
    if a < 100:
        print("a는 50보다 크고 100보다 작다")
    else:
        print("100보다 크다")
else:
    print("50보다 작다")

# 다중 if : if ~ elif ~ else

num = 90
if num >=90:
    print("등급 A",num)
elif num >=80:
    print("듭급 B",num)
elif num >=70:
    print("듭급 C",num)
elif num >=60:
    print("듭급 D",num)
else:
    print("듭급 E",num)

print()
age, height = 27, 180

if age >=20:
    if height >= 170:
        print('A 지망 가능')
    elif height >= 160:
        print('B 지망 가능')
    else:
        print('지원 불가')
else:
    print("20세 이상 지원 가능")


# 실습
# 사용자에게 점수를 입력 받고 학점 출력
# > 80 A학점, > 60 B학점, > 40 C학점, > 20 D학점, 나머지 E 학점
num = int(input("점수를 입력하세요 "))
if num > 80:
    print("A학점")
elif num > 60:
    print("B학점")
elif num > 40:
    print("C학점")
elif num > 20:
    print("D학점")
else:
    print("E학점")


# 사칙계산기
# 사용자에게 숫자 2개와 연산자(+, -, *, /, %, //, **) 입력 받은 후 연산을 한 후 결과 출력

num1 = int(input("첫번째 숫자 입력 "))
num2 = int(input("두번째 숫자 입력"))
c = input("연산자(+, -, *, /, %, //, **)를 입력하세요 ")

# 내 코드
if(c == "+"):
    print("{}{}{}={}".format(num1,c,num2,num1+num2))
elif(c == "-"):
    print("{}{}{}={}".format(num1,c,num2,num1-num2))
elif(c == "*"):
    print("{}{}{}={}".format(num1,c,num2,num1*num2))
elif(c == "/"):
    print("{}{}{}={}".format(num1,c,num2,num1/num2))
elif(c == "%"):
    print("{}{}{}={}".format(num1,c,num2,num1%num2))
elif(c == "//"):
    print("{}{}{}={}".format(num1,c,num2,num1//num2))
elif(c == "**"):
    print("{}{}{}={}".format(num1,c,num2,num1**num2))

# 수업 코드 - result 지정해서 깔끔해짐.
result = 0
if(c == "+"):
    result = num1 + num2
elif(c == "-"):
    result = num1 - num2
elif(c == "*"):
    result = num1 * num2
elif(c == "/"):
    result = num1 / num2
elif(c == "%"):
    result = num1 % num2
elif(c == "//"):
    result = num1 // num2
elif(c == "**"):
    result = num1 ** num2
else:
    print("연산자 확인")

print("{} {} {} = {}".format(num1,c,num2,result))

