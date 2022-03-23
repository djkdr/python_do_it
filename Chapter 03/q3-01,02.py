from re import I


a = "Life is too short, you need python"

if "wife" in a: print("wife")
elif "python" in a and "you" not in a: print("python")
elif "shirt" not in a: print("shirt")
elif "need" in a: print("need")
else: print("none")

result = 0
i = 1
while i <= 1000:
    if i%3==0:
        result += i
    i+=1
    
print(result)