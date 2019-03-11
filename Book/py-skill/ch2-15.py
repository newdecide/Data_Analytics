#15. 클로저가 변수 스코프와 상호 작용하는 방법
#19:41 ~ 

#1
def  sort_priority(values, group):
    def helper(x):
        if x in group:
            return (0,x)
        return (1,x)
    values.sort(key=helper)

numbers = [8,3,1,2,5,4,7,6]
group = {2,3,5,7}
sort_priority(numbers, group)
print(numbers)


#2 클로저 사용(스코프 버그 현상)
def sort_priority2(numbers, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return (0,x)
        return (1,x)
    numbers.sort(key=helper)
    return found

found = sort_priority2(numbers, group)
print('Found:', found)
print(numbers)

#3 데이터 얻어오기

def sort_priority3(numbers, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return (0,x)
        return (1,x)
    numbers.sort(key=helper)
    return found

# 헬버 클래스
class Sorter(object):
    def __init__(self, group):
        self.group = group
        self.found = False
    
    def __call__(self, x):
    
        self.found = True
        return (0,x)
    


