from collections import Counter

def count_words_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.lower()
    for char in ",.?!":
        text = text.replace(char, "")
    words = text.split()
    word_count = Counter(words)
    return word_count

file_path = "text.txt"
word_counts = count_words_from_file(file_path)
sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

print("Частота слів:")
for word, count in sorted_word_counts:
    print(f"{word}: {count}")
