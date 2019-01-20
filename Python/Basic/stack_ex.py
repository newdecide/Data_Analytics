#pop stack / pop(0) queue

word = "Hello, TEAMLAB"
word_list = list(word)
result = []

for _ in range(len(word_list)):
    result.append(word_list.pop())

print(result)