

def checkWord(word:str, required_letter:chr, available_letters:set) -> bool:
    """
    Returns true if the provided word will work
    Does not check word length, save time and only provide words 4 letter or longer
    """
    if required_letter in word:
        word_set = set(list(word))
        if len(word_set - available_letters) == 0:
            return True
        
    return False


