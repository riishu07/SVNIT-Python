import random
array = []
longest_zeroes_rows = []
zero_rows = 0 
for i in range (0,99):
    array.append(random.randint(0,1))
for j in range (0,99):
    if (array[j]==0):
        zero_rows+=1
    else:
        longest_zeroes_rows.append(zero_rows)
        zero_rows = 0

print("rows with the longest number of zeroes",max(longest_zeroes_rows))
print(array)

        
