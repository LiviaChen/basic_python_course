## 延續上一支程式
# 先擷取特定例外並處理，且將錯誤訊息中的資訊取出
###############
def createFile(name):
    try:
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except FileNotFoundError as e:
        print(e)
        print(e.args)
        name = name.replace('/', '')
        with open(name, 'w', encoding='utf-8') as f:
            f.write('123')
    except:
        print('Unexpected Error!')

createFile('test/test1')
###############

###############
def add(x, y):
    try:
        s = x + y
    except TypeError as e:
        try:
            s = int(x) + int(y)
        except ValueError as e_t:
            print('ValueError!')
            return None
        except:
            print('Unexpected Error!')
            return None
    except:
        print('Unexpected Error!')
        return None

    return s

output = add(3, '5')
print(output)

output2 = add(3, 'a')
print(output2)
###############

