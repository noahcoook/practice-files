def spam(divide_by):
    try:
        return 42 / divide_by
    except ZeroDivisionError:
        print('Error: Invalid argument.')
print(spam(2))
print(spam(423))
print(spam(42))
print(spam(4))
print(spam(0))

