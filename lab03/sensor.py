porog = int(input())
n = int(input())
error = 0
prev = 0
maxim = -10 ** 19
sred = 0.0
for i in range(n):
    x = input()
    if x == 'error':
        error += 1
    else:
        sred += float(x)
    if x != 'error' and float(x) > porog:
        prev += 1
    if x != 'error' and float(x) > maxim:
        maxim = float(x)
print(f'{n}')
print(f'{error}')
print(f'{prev}')
print(f'{maxim:.1f}')
print(f'{(sred/(n-error)):.1f}')
