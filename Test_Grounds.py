num = 543

print('before: ', num)
_len = len(str(num))
_len -= 1
print('len: ', _len)
digit = num % 10
num //= 10
num += (digit * 10**_len)

print('after: ', num)
