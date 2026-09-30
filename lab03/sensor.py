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
