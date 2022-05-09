a = [1,2,3]

try:
    a[4]

except IndexError as e:
    print(e)
