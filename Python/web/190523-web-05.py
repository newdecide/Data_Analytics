#coding=utf-8
#파일 입출력

# f = open('파일 경로', '모드')
# f.close()
#파일을 연 후에는 닫아야 함. 메모리에 올라가 있기 때문이다. 

#상대경로 / 절대경로
# 3가지 모드
# w : write
# r :read
# a :append

#.은 현재 폴더를 말을 함

f = open("./hello.txt", "w")
f.write("Hello World")
f.close()


f2 = open("./hello.txt", "a")
for i in range(2, 11):
    content = '\n' + str(i) + "번째 줄입니다."
    f2.write(content)
f2.close

