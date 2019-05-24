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

# f = open("./hello.txt", "w")
# f.write("Hello World")
# f.close()


# f2 = open("./hello.txt", "a")
# for i in range(2, 11):
#     content = '\n' + str(i) + "번째 줄입니다."
#     f2.write(content)
# f2.close

# f3 = open("./hello.txt", "r")
# context = f3.read()
# print(context)
# #seek을 통해서 커서를 바꿔서 또 다시 올수 있다. 
# f3.close

#ex) 파일 만들고 읽어오기

# f = open("./helloworld.txt", "w")
# for i in range(1, 11):
#     f.write("Hello World \n" )
# f.close()

# f = open("./helloworld.txt", "a")
# for i in range(1, 11):
#     f.write("Hello Python \n")
# f.close()

# f = open("./helloworld.txt", "r")
# for i in range(1, 11):
#     f.readline()

# f.seek(0)
# f.read()
# f.close()

# #csv 파일 만들어서 파일 저장하기
# import pprint
# values = [{
#     "name" : "hsy",
#     "phone" : "010-4111-0256",
#     "city" : "seoul"
# } for _ in range(3)]

# def to_csv(value):
#     #키 값 분류
#     keys = []
#     for el in value[0]:
#         keys.append(el)
    
#     #벨류값 분류
#     results = []
#     for d in value:
#         result =[]
#         for el in d.values():
#             result.append(el)
#         results.append(result)
    
#     #CSV 정규표현식 
#     content = ', '.join(keys) + '\n'
#     for result in results:
#         content += ', '.join(result) + '\n'
    
#     #저장
#     f = open ('./csv_file.txt', 'w')
#     f.write(content)
#     f.close

# #함수 활용
# to_csv(values)       

f = open("./csv_file.txt", "r")
fs = f.read()
f.close 

for i in fs:
    print(i)

# def to_dict(csvs):
    