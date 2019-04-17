#9:30 ~ 10:00 
#1부터 100까지의 합

sum = 0
for i in range(101):
    sum+=i
print("1부터 100까지의 합: {}".format(sum))

for i in range(101):
    sum += i
print(sum)


#11:13~ 
#O(N)
for i in range(101):
    sum = sum +i

#O(N*N)
for i in range(N):
    for j in range(N):
        k = k +1

#O(N*N*N)
for i in range(N):
    for j in range(N):
        for k in range(N):
            s = s +1 

#반복문이 떨어져서 2개 이상 있는 경우 
# 가장 큰 값을 계산함
for i in range(N):
    sum = sum + 1
    i = 0

for i in  range(N):
    for j in range(N):
        k = k+1

# 알고리즘 성능에 if - else 문은 성능에 영향을 미치지 않음

# 재귀 호출은 풀어서 계산 한다.
# 팩토리얼을 재귀 호출에 사용하는 프로그램

def fact(int N):
    if N <= 1:
        return 1
    else: 
        return N * fact(N-1)

#알고리즘 최적화(01)
def max_sum(N):
    sum = max = 0
    
    for i in range(N):
        for j in range(N):
            sum = 0
            for k in range(i, j+1):
                sum = sum + data[k]
            if sum > max:
                max = sum
    return max

print(max_sum(1))