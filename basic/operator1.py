# 연산자
# 산술연산자 : +,-,*,/(실수),//(정수),%, **
a,b = 5,3
print(a+b,a-b,a*b,a/b,a//b,a%b,a**b)

print()
s1,s2,s3 = "100","100.123","999999999"
print(s1+s2+s3)
print(float(s1)+float(s2)+float(s3))
print(int(s1) + 1)   # TypeError: can only concatenate str (not "int") to str

# 복합대입연산자 : +=, -=, *=, /=, //=, %=, **=
a = 10
a += 5
print("a",a)
a == 5
print("a",a)
a *= 5
print("a",a)
a /= 5
print("a",a)
a //= 5
print("a",a)
a %= 5
print("a",a)
a **= 5
print("a",a)

# 실습 : 777,777 원
# 화폐교환 : 5만원/1만원권/5천원/1천원
money = 777777
ex_50000 = money // 50000
money %= 50000
ex_10000  = money // 10000
money %= 10000
ex_5000  = money // 5000
money %= 5000
ex_1000  = money // 1000
money %= 1000

print("50,000원 : %d 장" % ex_50000)
print("10,000원 : %d 장" % ex_10000)
print("5,000원 : %d 장" % ex_5000)
print("1,000원 : %d 장" % ex_1000)


# 관계연산자 : ==, !=, >, <, >=, <=
a,b = 10,0
print(a==b, a!=b, a>b, a<b, a>=b, a<=b)

# 논리연산자 : and, or, not
print(100 > 60 and 60 > 15)
# print(100 > 60 && 60 > 15)  # &&로 사용 못함
print(100 > 60 or 60 > 15)
print(not 60 < 15)
print(not False)
print(not True)
# print(!True)  # !로 부정표현 못함

# 비트연산자
print(10 & 7)
print(10 | 7)
print((100>60) & (60 > 15))







