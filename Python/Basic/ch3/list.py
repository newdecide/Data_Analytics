#리스트(시퀀스 자료형, 여러 데이터들의 집합)

colors = ['red', 'blue']

print(colors[0])
print(colors[1])

#Slicign(슬라이싱) list 값들을 잘라서 쓰는 것
cities = ['서울', '인천', '부산', '대구', '대전', '광주', '울산', '수원']

print(cities[0:6], "AND", cities[-9:])
print(cities[:])
print(cities[-50:50])
print(cities[::2],"and", cities[::-1])

#길이 
print(len(color))

#리스트 값 변경
colors[0] = "yellow"
print(colors)

#리스트 추가
colors.append("red")
print(colors)

colros2 = ["orange"]

#값 자체가 변홤 
colors.extxend(colors2)

#값 삭제 
del colors[0]

#변수의 타입은 실행 시점에 됨.

#패킹   
t = [1,2,3]

#언패킹
a, b, c = t

print(a,b,c)




