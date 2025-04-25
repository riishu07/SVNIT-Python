def capital(w):  
    result = ""  
    
    for i in range(len(w)):  
        if i % 2 == 0:  
            result += w[i].lower()  
        else:  
            result += w[i].upper()  
    
    return result  

word = input("Please enter a word: ")  
capitalized_word = capital(word)  
print(capitalized_word)
