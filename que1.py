def vowel(word):
    word_count=0
    vowel_letter=['a','e','i','o','u']
    for i in vowel_letter:
        if i in word:
            word_count+=1
    print(word_count)
 
vowel('kush')