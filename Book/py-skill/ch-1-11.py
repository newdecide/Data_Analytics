#이터레이터를 병렬로 처리하면 zip을 사용하자

#1) 리스트 컴프리헨션
names = ['Cecilia', 'Lise', 'Marie']
letters = [len(n) for n in names]
print("c1:",letters)

#2)if
longest_name = None
max_letters = 0
for i in range(len(names)):
    count = letters[i]
    if count > max_letters:
        longest_name = names[i]
        max_letters = count

print("c2:", longest_name)

#3) enumerate
for i , name in enumerate(names):
    count = letters[i]
    if count > max_letters:
        longest_name = name
        max_letters = count

print("c3:" ,longest_name)

#4) zip => 튜플로 저장 됨.
#제너레이터가 아니기 때문에 반환하는 작업을 해야함
for name, count in zip(names, letters):
    if count > max_letters:
        longest_name = name
        max_letters = count

#5) 추가 한 값이 아닌 리스트 컴프리헨션한 값만 들어온 것을 알 수 있음.
names.append('Rosalind')
for name, count in zip(names, letters):
    print("c5:", name)