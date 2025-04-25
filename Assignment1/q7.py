list = [[],[],[],[],[]]
for i in range (1,11):
    list[i%5].append(i)
for i in range (0,5):
    print("List of numbers with remainder ",i)
    print(list[i])
