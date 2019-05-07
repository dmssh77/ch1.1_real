# 치환문

a = 1

b = a + 1

print(a, b, sep="                ")

# 여러 개를 한번에 치환
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 할당
x = y = z = 10
print(x, y, z)

# C 스타일로 지원 안한다우
# x = (y = 10)

# swap
x = 1
y = 2
print(x, y)

#temp = x
#x = y
#y = temp

x, y = y, x

print(x, y)

# 동적 타이핑
a = "Hello"
print(type(a))

# 확장 치환문
a = 10
a += 10
a -= 5
print(a)