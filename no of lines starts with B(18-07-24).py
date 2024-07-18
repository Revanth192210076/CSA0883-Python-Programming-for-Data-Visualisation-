def count_sentences_starting_with_b(text):
    sentences = text.split('.') 
    count = 0

    for sentence in sentences:
        if sentence.strip().startswith('B') or sentence.strip().startswith('b'):
            count += 1

    return count

text = """
Bobby likes bananas. He buys them from the store. But sometimes he prefers apples.
Bananas are his favorite fruit.
"""

result = count_sentences_starting_with_b(text)
print(f"Number of sentences starting with 'B': {result}")
