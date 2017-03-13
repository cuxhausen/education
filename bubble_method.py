

list1 = [1, 2, 3, 8, 14, 89, 45] 

n = 1

while n < len(list1):
	for i in range(len(list1) - n):
		if list1[i] > list1[i + 1]:
			list1[i], list1[i + 1] = list1[i + 1], list1[i]
	n += 1

print (list1)