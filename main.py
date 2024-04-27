import time

letters = 'abcdefghijklmnopqrstuvwyxzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
chars = ' `~!@#$%^&*()_+-=[]\\;\'",./{}|:"<>?'
lnc = letters + numbers + chars

message = input('message : ')
result = str()

for i in message:
    for j in lnc:
        result += j
        print(result)
        if i == j:
            break
        else:
            result = result[:-1]
        time.sleep(0.005)