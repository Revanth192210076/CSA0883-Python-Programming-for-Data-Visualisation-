def sort_letters(word):
    
    sorted_word = ''.join(sorted(word))
    print(f"Alphabetically sorted (Normal order): {sorted_word}")

    sorted_word_reverse = ''.join(sorted(word, reverse=True))
    print(f"Alphabetically sorted (Reverse order): {sorted_word_reverse}")

word = "revanth"
sort_letters(word)
