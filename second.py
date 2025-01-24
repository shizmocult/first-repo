from collections import Counter

def count_words_from_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        words = text.lower().split()
        words = [word.strip(",.?!") for word in words]
        word_count = Counter(words)
        return word_count
    except FileNotFoundError:
        print(f"Файл '{file_path}' не знайдено.")
        return None
    except Exception as e:
        print(f"Сталася помилка: {e}")
        return None

file_path = "text.txt"
word_counts = count_words_from_file(file_path)

if word_counts:
    for word, count in word_counts.items():
        print(f"{word}: {count}")
