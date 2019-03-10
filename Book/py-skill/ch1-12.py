#for와 while 루프 뒤에는 else 블록을 쓰지 말자
#21:12 ~ 21:40

#1 else 문이 실행이 됨.
for i in range(3):
    print('ch1 :','Loop %d ' %  i)
else:
    print('ch1 :','Else block')

#2 else 문을 건너 뜀.
for i in range(3):
    print('ch2 :', 'Loop %d' % i)
    if i == 1:
        break
else:
    print('ch2 :','Else block')

#3 빈 시퀀스 처리시 else 바로 실행됨.
for x in []:
    print('ch3 :','Never runs')
else:
    print('ch3 :','For Else block!')

#4 while, 처음부터 거짓일 때 실행
while False:
    print('ch4 :','Never runs')
else:
    print('ch4 :','While Else block')

#5 공약수를 구하기
#공약수: 1밖에 없는 둘 이상의 수 
#계산하는 헬버함수로 바꿔라.
a = 4
b = 9
for i in range(2, min(a,b)+1):
    print('ch5 :','Testing', i)
    if a % i == 0 and b % i == 0:
        print('ch5 :','Not coprime')
        break
else:
    print('ch5 :','Coprime')

#5-1 헬버함수
def coprime(a,b):
    for i in range(2, min(a,b)+1):
        if a % i == 0 and b % i == 0:
            return False
        return True

print('ch5-1:',coprime(a,b))

def coprime2(a,b):
    is_coprime = True
    for i in range(2, min(a, b)+1):
        if a % i == 0 and b % i ==0:
            is_coprime =False
            break
        return is_coprime

print('ch5-2:',coprime2(2,3))
