from tqdm import tqdm
import re

src_file = "pg29765.txt"
dest_file = "gute_four.txt"

with open(dest_file, "w") as out_file:
    line_count = 0
    with open(src_file, "r") as in_file:
        for line in in_file:
            line_count += 1

    with open(src_file, "r") as in_file:
        # Words are on a line by themselves and all capital, so we look for anything not a capital letter
        regex = re.compile(r"[^A-Z]")
        pb = tqdm(total=line_count, desc="Processing", unit="lines")
        for line in in_file:
            line = line.strip()
            if regex.search(line) is None:
                if len(line) >= 4:
                    out_file.write(f"{line.lower()}\n")
            pb.update()
        pb.close()


        
            



