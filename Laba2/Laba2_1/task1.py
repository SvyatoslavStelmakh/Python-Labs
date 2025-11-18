text = input("Введите текст, отделяя слова пробелами.\n")

words = text.lower().split()
    
word_dict = {}
    
for word in words:
        
    word = word.strip('.,!?;:"()[]')    # убираем возможные знаки препинания вокруг слов
        
    if word:                            # проверяем, что слово не пустое после очистки
        word_dict[word] = word_dict.get(word, 0) + 1

unique_words = 0

print("Словарь {слово: количество}:")
for word, count in word_dict.items():
    print(f"   '{word}': {count}")
    if count == 1:
        unique_words += 1

print("Количество уникальных слов: ", unique_words)

