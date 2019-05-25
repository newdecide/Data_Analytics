#coding=utf-8

a = lambda x : x + 1

b = lambda a, b, c : a + b +c
c = lambda a, b : a*a + b*b

print(a(4))

print(b(1,2,3))
print(c(2,4))

d = lambda a : True if a % 2 == 0  else False
print(d(3))
print(d(4))

e = lambda *a : sum(a)

print(e(1,2,3,4,5))

# map

a = list(range(1, 11))
result = []

for el in a:
    result.append(el+1)
