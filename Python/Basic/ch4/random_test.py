# 1~100 임의 숫자를 맞추시오

import random
guess_number = random.randint(1, 100)
print(guess_number)

print("숫자를 맞춰보세요.")
user_input = int(input("숫자를 입력하세요."))
while (user_input is not guess_number):
    if user_input > guess_number:
        print("숫자가 너무 큽니다.")
    else:
        print("숫자가 너무 작습니다.")
    user_input = int(input())
else:
    print("정답입니다.", user_input, "입니다.")