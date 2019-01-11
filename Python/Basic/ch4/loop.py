# for 문        

for looper in [1,2,3,4,5]:
    print("hello")
for looper in range(0,5):
    print("hello")
for i in range(1, 10, 2):
    print(i)

for i in range(10,1,-1):
    print(i)

#while 문(~동안)
# i = 1
# while i < 10:
#     print(i)
#    # i+1

for i in range(0,5):
    print(i)

i=0
while i < 5:
    print(i)
    i = i + 1    

#break 문
for i in range(10):
    if i == 5: break
    print(i)
print("EOP")

#continue 특정 조전에서 남은 반복 명령  
for i in range(10):
    if i == 5: continue
    print(i)
print("EOP")

