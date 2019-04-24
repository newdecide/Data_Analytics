#try/except/else/finally에서 각 블록의 장점을 이용하자
# 21:40 ~ 21:54
# #1 finally 블록
# handle = open('/tmp/random_data.txt')
# try:
#     data = handle.read()
# finally:
#     handle.close()

#else 블록
def load_json_key(data, key):
    try:
        result_dict = json.loads(data)
    except ValueError as e:
        raise KeyError from e
    else:
        return result_dict[key]

#3) 모두 사용
UNDEFINED = object()

def divide_json(path):
    handle = open(path, 'r+')
    try:
        data = handle.read()
        op = json.loads(data)
        value = (
            op['numerator'] /
            op['denominator'])
    except ZeroDivisionError as e:
        return UNDEFINED
    else:
        op['result'] = value
        result = json.dumps(op)
        handle.seek(0)
        handle.write(result)
        return Value 
    finally:
        handle.close()
    print("1")
