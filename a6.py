N = int(input("Введите время:"))
h = N // 3600
m = (N % 3600) // 60
s = N % 60
print('{}:{:02}:{:02}'.format(h, m, s))