# WordBeeSolver
 Find as many words as possible from 7 letters (https://www.nytimes.com/puzzles/spelling-bee)

 Usage:
 python3 WordBeeSolver.py \[required letter] \[available letters]

 The yellow honeycomb letter is the required one and the available letters are the ones around it

 Example (for 11/4/2023):

 python3 WordBeeSolver.py b lieokm

 It will provide you a list of words, sorted in descending length, that can be used.  Words with a "*" in front are "pangram" words worth more points!

 This tool is only as good as its word list.  The word list that comes with the repository is every word found at https://www.gutenberg.org/ebooks/29765 that is 4 or more letters long.  Its a pretty good list but it STILL falls short.

 For instance for the puzzle on 11/4/2023 perhaps the best word is "bookmobile" (Found with this tool, I take no credit).  However, "bookmobile" does not appear to be in the version of Webster's Dictionary hosted at the site referenced above.  (Though I added to the end just because)

 Also, a LOT of words in that dictionary appear to not be in the word list for the game.  However, if I use the word list that had "bookmobile" in it, there were even more words that were not real.

 So, you can specify your own word list if you would like with --wordlist:

 python3 WordBeeSolver.py --wordlist yourlist.txt b lieokm

 Your word list should be a simple text file with one word on each line.

 Have fun! 
