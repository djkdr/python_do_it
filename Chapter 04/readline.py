f = open("doit/새파일.txt", 'r', encoding='utf8')
# lines = f.readlines()
# for line in lines:
#     print(line)
data = f.read()
print(data)
f.close()