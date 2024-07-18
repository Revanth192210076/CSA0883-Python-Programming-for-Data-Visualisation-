def remove_common_words(S1, S2):

    words_S1 = set(S1.split())
    words_S2 = set(S2.split())

    common_words = words_S1.intersection(words_S2)

    result_S1 = ' '.join(word for word in S1.split() if word not in common_words)
    result_S2 = ' '.join(word for word in S2.split() if word not in common_words)

    return result_S1, result_S2

S1 = "Revanth Harsha Vardhan"
S2 = "Boppudi Revanth"

output_S1, output_S2 = remove_common_words(S1, S2)
print(f"Output S1: {output_S1}")
print(f"Output S2: {output_S2}")
