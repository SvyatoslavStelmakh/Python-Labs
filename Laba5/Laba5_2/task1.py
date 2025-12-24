def count_words(sentence):

    if not sentence or sentence.isspace():
        return 0
    
    words = sentence.strip().split(" ")
    return len(words)
