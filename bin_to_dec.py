
x = str(input("Введите число в двоичной системе исчисления (без 0b в начале): "))
n = 0
i = -1
j = 0
p = int(x[i]) 
for i in x:
	n = n + p * 2**j
	i = i - 1
	j = j + 1

print (n)
