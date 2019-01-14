print("구구단 몇단을 계산 할까요?")
x = 1
while (x is not 0) :
    x = int(input())
    if x == 0: break
    if not(1 <= x <= 9):
        print("잘못 입력하셨습니다.")
        continue
    else:
        print("구구단 ",x,"단을 게산 합니다.")
        for i in range(1,10):
            print(x, "*", i)
        print("구구단 몇 단을 계산할까요?")
print('구구단 종료')            
    
