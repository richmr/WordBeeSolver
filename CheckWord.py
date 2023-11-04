

def checkWord(word:str, required_letter:str, available_letters:set) -> bool:
    """
    Returns true if the provided word will work
    Does not check word length, save time and only provide words 4 letter or longer
    """
    if required_letter in word:
        word_set = set(list(word))
        if len(word_set - available_letters) == 0:
            return True
        
    return False


def perfectWord(word:str, required_letter:str, available_letters:set) -> bool:
    """
    Returns true if the word uses all available letters
    """
    word_set = set(list(word))
    if len(available_letters - word_set) == 0:
        return True
    return False

