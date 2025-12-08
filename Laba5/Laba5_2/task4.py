def are_anagrams(word1, word2):
    word1 = str(word1).lower()
    word2 = str(word2).lower()
    
    if len(word1) != len(word2):
        is_anagram = False

    is_anagram = sorted(word1) == sorted(word2)
    return is_anagram