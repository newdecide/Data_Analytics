#None을 반환하기 보다는 예외를 일으키자
# 21:55~

#1. 숫자를 나누는 헬버함수
# def divide(a, b):
#     try:
#         return a /b
#     except ZeroDivisionError:
#         return None

# result = divide(x, y)
# if result is None:
#     print('ch1 :','Invalid inputs')

#2. 0이 되어버림

# x,y = 0, 5
# result = divide(x,y)
# if not result:
#     print('ch2: ','Invalid inputs')

def divide(a,b):
    try: 
        return a/b
    except ZeroDivisionError as e:
        raise ValueError('Invalid inputs') from e

# _, result = divide(x,y)
# if not result:
#     print('Invalid inputs')

x, y = 5,2
try:
    result = divide(x,y)
except ValueError:
    print('Invalid inputs')
else:
    print('Result is %.1f' % result)
