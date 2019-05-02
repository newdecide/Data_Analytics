#16. 리스트를 반환하는 대신 제너레이터를 고려하자
def index_words(text):
    result = []
    if text:
        result.append(0)
    for index, letter in enumerate(text):
        if letter == ' ':
            result.append(index + 1)
    return result

address = 'Four score and seven years ago...'
result = index_words(address)

# 17. 이중연결리스

