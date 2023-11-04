from tqdm import tqdm


with open("fourPlusWords.txt", "w") as out_file:
    with open("mitwordlist.txt", "r") as in_file:
        for i, word in enumerate(tqdm(in_file)):
            word = word.strip()
            if len(word) >= 4:
                out_file.write(f"{word}\n")


