#coding=utf-8

print(1 + 3)
print("Hello World")

if 3 > 5:
    print("3은 5보다 큽니다")

print("여기는?")

#1-06 문제 랜덤 숫자 맞추기

import random 

n = random.randint(1,100)
print(n)

s = int(input())

d = n - s 

if n == s:
    print("정답")
elif d <= 10:
    print("아깝네요")
elif d >= 10:
    print("틀렸습니다.")

# #1-06(2) 
#1 부터 100까지 출력하시오
for s in range(1,101):
    print(s)



while True:
    print("실행")
