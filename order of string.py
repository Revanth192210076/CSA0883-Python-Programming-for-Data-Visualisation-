def arrange_letters(word):
   
    letters = list(word)
    normal_order = sorted(letters)
    normal_order_str = ' '.join(normal_order)
    reverse_order = sorted(letters, reverse=True)
    reverse_order_str = ' '.join(reverse_order)
    
    print(f'Normal order: {normal_order_str}')
    print(f'Reverse order: {reverse_order_str}')


if __name__ == "__main__":
    word = input("Enter the word: ").upper()
    arrange_letters(word)
