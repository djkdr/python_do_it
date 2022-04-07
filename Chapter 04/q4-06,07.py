user_input = input("저장할 내용을 입력하세요:")
f = open('doit/문제5.txt', 'a', encoding='utf8')
f.write(user_input)
f.write("\n")
f.close()

#####################################

g = open('test.txt', 'r')
body = g.read()
g.close()

body = body.replace('java', 'python')

g = open('test.txt.', 'w')
g.write(body)
g.close()
