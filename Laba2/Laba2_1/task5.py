word1 = input("Введите первое слово: ")
word2 = input("Введите второе слово: ")

word1 = word1.lower()
word2 = word2.lower()
    
if len(word1) != len(word2):
    is_anagram = False

is_anagram = sorted(word1) == sorted(word2)

if is_anagram == True:
    print("Слова явлются анаграммами!")
else:
    print("Слова НЕ явлются анаграммами!")
