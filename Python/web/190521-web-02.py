#coding=utf-8
#15:30 
#Dict, Tuple

list1 = [1,2,3,4,5]
print(list1)

#1~100까지 숫자를 튜를로 만들기

#list
value =[]

for i in range(1, 101):
    value.append(i)

#Tuple
tuple_1_to_100 = tuple(range(1,101))

print(tuple_1_to_100)

#튜플을 사용해서 정보 입력
my_info = [('이름', '시연'), ('이메일', 'lowgiant@gmail.com'), ('연락처', '010-4111-0256'), ('나라', 'Korea')]

print(my_info) 

#dict 만들기
d = {}
print(type(d))

d['name'] = 'sol'

print(d)

print(d['name'])

s = d.get('name')

print(s)

#딕셔너리로 정보 만들기
in_fo = {
    'name' : '시연',
    'age' : '29',
    'phone': '010-4111-0256' 
}

in_fo['email'] = 'newreview@naver.com'

print(in_fo)

for el in in_fo:
    print(el, end=' : ')
    print(in_fo[el])


#리스트 값 정리
my_info = [
    ('nickname', 'cocolman'), ('country', 'korea'), ('name', 'sol')
]

print(dict(my_info))




