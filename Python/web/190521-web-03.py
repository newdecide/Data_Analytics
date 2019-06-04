

#str 타입 csv으로 변경
csv_values = """
이름, 연락처, 나이, 이메일
철수, "010-1234-4567", 23, "chulsu@gmail.com"
영희, "010-1234-2345", 30, "234@naver.com"
"""

#첫과 마지막 줄을 지워죠.
csv_values = csv_values.strip('\n')
#스티링
csv_list = csv_values.split('\n')

print(csv_list)

# key 값 리스트 만들기
keys = []

for el in csv_list[0].split(','):
    keys.append(el.strip(' '))

print(keys)

results = []
for val in csv_list[1:]:
    result_dict = {}
    i = 0
    for el in val.split(','):
        result_dict[keys[i]] = el
        i += 1
    results.append(result_dict)
print(results)


#Set 데이터 구조
#집합
#union 합집합
#different 차집합(-연산자를 사용해도됨.)
#interserction(교집합)
#100의 수 중 3, 5, 15 배수 만들기 

set1 = set()
set2 = set()
set3 = set()

for i in range(1, 101):
        
    if i % 3 == 0:
        set1.add(i)
    if i % 5 == 0:
        set2.add(i)
    if i % 15 == 0:
        set3.add(i)
    
print(set1)
print(set2)
print(set3)

#List commpise

a = []
for i in range(1,11):
    a.append(i**2)
print(a)

a2 = [ i for i in range(1, 10+1) if i % 2 ==0]

print(a2)
# 리스 정보
# ..