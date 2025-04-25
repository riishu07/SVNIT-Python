def biggerIsGreater(word):
    word = list(word)
    n = len(word)
    pivot = -1
    
    for i in range(n - 2, -1, -1):
        if word[i] < word[i + 1]:
            pivot = i
            break
    
    if pivot == -1:
        return "nil"
    
    for i in range(n - 1, pivot, -1):
        if word[i] > word[pivot]:
            break
    
    word[pivot], word[i] = word[i], word[pivot]
    
    
    word[pivot + 1:] = sorted(word[pivot + 1:])
    
    return ''.join(word)

testCase = int(input("Enter number : "))
for i in range(testCase):
    word = input().strip()
    result = biggerIsGreater(word)
    print(result)