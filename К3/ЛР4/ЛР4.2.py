 
	import os

# имя папки проекта
PROJECT_NAME = "word_project"

# создаём папку проекта
os.makedirs(PROJECT_NAME, exist_ok=True)

# file_reader.py
file_reader_code = '''def read_file(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return f.read()
'''

word_counter_code = '''def count_words(text):
    words = text.lower().split()

    freq = {}
    for word in words:
        if word in freq:
            freq[word] += 1
        else:
            freq[word] = 1

    return freq
main_code = '''from file_reader import read_file
from word_counter import count_words

text = read_file("text.txt")
word_freq = count_words(text)

top_10 = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)[:10]

print("Топ-10 слов:")
for word, count in top_10:
    print(word, "-", count)
text_content = '''Python is easy and Python is powerful
Python is good for beginners
'''

files = {
    "file_reader.py": file_reader_code,
    "word_counter.py": word_counter_code,
    "main.py": main_code,
    "text.txt": text_content
}
for filename, content in files.items():
    with open(os.path.join(PROJECT_NAME, filename), "w", encoding="utf-8") as f:
        f.write(content)

print(" Проект создан!")
print(" Папка:", PROJECT_NAME)
print(" Запусти: python main.py")

