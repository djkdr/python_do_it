def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False


is_odd(3)


def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result/len(args)


avg_numbers(1, 2)


avg_numbers(1, 2, 3, 4, 5)


input1 = input("첫번째 숫자를 입력하세요:")
input2 = input("두번째 숫자를 입력하세요:")

total = int(input1)+int(input2)
print("두 수의 합은 %d 입니다." % total)
