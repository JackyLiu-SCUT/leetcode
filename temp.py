import chardet

f = open('temp','rb')
data = f.read()
print(chardet.detect(data))
# data = data.sp
print(data.decode('utf-8'))

print(b'\\u6211'.decode('utf-8'))