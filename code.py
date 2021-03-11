def vowel_check(word):
       
    new = ''
    for _ in word:
        if _ == 'a'or _ == 'e' or _ == 'i' or  _ == 'o' or _ == 'u':
            new = new + _.upper()
        else:
            new = new + _.lower()
    print(f'{new}')
    
vowel_check(input("Enter a word: ")  
