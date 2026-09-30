porog = int(input())
n = int(input())
error = 0
prev = 0
maxim = 0.0
sred = 0.0
for i in range(n):
    x = input()
    if x == 'error':
        error += 1
    if x != 'error':
        sred += float(x)
    if x != 'error' and float(x) > porog:
        porog += 1
    if x != 'error' and float(x) > maxim:
        maxim = float(x)
print(n, error, prev, maxim, (sred/(n-error)))
