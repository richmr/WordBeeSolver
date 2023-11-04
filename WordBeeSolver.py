import typer
from typing import Optional
from typing_extensions import Annotated
from pathlib import Path
from tqdm import tqdm

from CheckWord import checkWord, perfectWord

def reqLet(value:str) -> str:
    """
    Checks to make sure the require letter is only a single letter and also makes sure it is lower case
    """
    if not len(value) == 1:
        raise typer.BadParameter(f"There should only be a single required letter not {len(value)}.")
    
    return value.lower()

def availLetters(value:str) -> str:
    """
    Checks to make sure there are 6 available letters and also makes sure it is lower case
    """
    if not len(value) == 6:
        raise typer.BadParameter(f"There should be 6 required letters not {len(value)}.")

    return value.lower()

def checkfile(file_p:Path) -> Path:
    # Check wordlist exists
    if not file_p.is_file():
        raise typer.BadParameter(f"{file_p} not found.  Please provide a path to a valid word list (text file, one word per line) with --wordlist filename")
        
    return file_p

def solver(requiredletter: Annotated[str, typer.Argument(
                                                    help="The required letter (it's in the middle)",
                                                    callback=reqLet)], 
           availableletters: Annotated[str, typer.Argument(
                                                    help="The letters around the middle one",
                                                    callback=availLetters)],
           wordlist:Annotated[Optional[Path], typer.Option(
               help="Path to word list to use.  Expects .txt files with one word per line",
               callback=checkfile,
               file_okay=True,
               dir_okay=False)] = "gute_four.txt"):
    """
    Produces a word list of words that solve the Word Bee problem.
    Sorts by longest words first.
    Words that use all the letters are marked by a *
    """   
    
    # Get the length of the wordlist for progress bar purposes
    number_of_words = 0
    with wordlist.open() as wl:
        for i, word in enumerate(wl):
            number_of_words += 1
    
    found_words = []
    avail_letters_set = set(list(availableletters))
    # add the required letter into the set for later comparison
    avail_letters_set.add(requiredletter)    
    with wordlist.open() as wl:
        pb = tqdm(total=number_of_words, desc="Scanning word list", unit="words")
        for word in wl:
            word = word.strip()
            if checkWord(word, requiredletter, avail_letters_set):
                if perfectWord(word, requiredletter, avail_letters_set):
                    found_words.append(f"* {word}")
                else:
                    found_words.append(word)
            pb.update()
        pb.close()

    found_words = sorted(found_words, key=len, reverse=True)
    print(f"Found {len(found_words)} words")
    for word in found_words:
        print(word)
    
    
   

if __name__ == "__main__":
    typer.run(solver)

    typer.Argument()