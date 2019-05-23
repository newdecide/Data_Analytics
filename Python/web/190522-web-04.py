#coding=utf-8

#16:30
#함수

#추상화: 별도에 공간에 존재하여, 변수간 간섭되는 방해를 일으키지 않는 방법
#분리: 코드는 다른 곳에 

#Hello_world 함수
def print_hello_world():
    print("Hello World")
print_hello_world()

#add 함수
def add(a,b):
    return a + b

print(add(5,5))

# 숫자에 1을 추가 하는 함수
def number_1(a):
    return a + 1

print(number_1(4))

# 문자열에 느낌표 추가하기
def str_d(a):
    return a + "!"

print(str_d("def"))

def op():
    d = input('1부터 9까지 숫자를 선택하세요.')
    return int(d)

def input_like():
    likes = []
    like = input("좋아하는 것을 하나 입력하세요.")
    likes.append(like)
    print

#재귀 함수 
#함수를 다시 불러오는 것
def factorial(n):
    result =1
    for i in range(1, n+1):
        result *= i
    return result

#예외처리
#try
#except: 

try:
    num= input('숫자로 입력하세요.')
    num = int(num)
    print(num+2)
except:
    print("숫자를 숫자키로 입력하세요. 한글로 말고요")

