def count_words_and_lines(paragraph):
    lines = paragraph.splitlines()  
    num_lines = len(lines)  

    for i, line in enumerate(lines, start=1):
        words = line.split()  
        num_words = len(words)  
        print(f"Line {i}: {num_words} words")

    print(f"\nTotal number of lines: {num_lines}")

# Example usage:
paragraph = """
This is a sample paragraph
consisting of multiple lines
each with varying number of words.
Counting them is fun!
"""

count_words_and_lines(paragraph)
