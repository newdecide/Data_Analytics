
#구구단 만들기
i = int(input())
print("구구단 몇답을 계산 할까요", i)

print("구구단"+ str(i) +" 단을 계산합니다.")

for x in range(1, 10):
    print(str(i)+" x "+str(x)+" = "+str(i*x) )
