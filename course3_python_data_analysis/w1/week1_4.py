def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    max_letter = ''
    max_num = 0
    
    for letter in ALPHABET:
        for word in word_list:
            count_ltr = word.count(letter)
            if letter_count.get(letter) == None:
                letter_count[letter] = count_ltr
            else:
                letter_count[letter] += count_ltr
        if letter_count[letter] > max_num:
            max_letter = letter
            max_num = letter_count[letter]
                
    return(max_letter, max_num)
        
        
    # enter code here
    
print(count_letters(["hello", "world"]))

monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"
monty_words = monty_quote.split(" ")
print(count_letters(monty_words))