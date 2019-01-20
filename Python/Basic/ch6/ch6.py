a = "abcd e f g"
b = a.split()
c = (a[:3][0])
d = (b[:3][0][0])
print(c + d)

#2

number = "100"

def midterm(number):
    result = ""
    if number.isdigit() is True:
        if number is 100:
            if number/10 == 1:
                result = True
            else:
                result = False
    return result

print(midterm(number))
