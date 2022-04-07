print("you" "need" "python")

print("you"+"need"+"python")

print("you", "need", "python")

print("".join(["you","need","python"]))

#####################################

f1 = open("doit/문제5.txt", 'w', encoding='utf8')
f1.write("Life is too short")
f1.close()

f2 = open("doit/문제5.txt", 'r', encoding='utf8')
print(f2.read())
f2.close()