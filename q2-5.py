from dataclasses import replace


a="a:b:c:d"
b=a.replace(":", "#")
print(b)