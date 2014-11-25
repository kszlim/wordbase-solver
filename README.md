I apologize for the messy state of things, I'll probably clean it up a lot later.

Replace the string in board.txt with the representation of your board.

Run wordbase.py to access the interface, wait for it to load the dictionary.

use words_at_coordinate(trie, board, (X, Y), DEPTH) in order to get the list of possible words at that coordinate.

DEPTH should be an integer that specifies the maximum length of word to search for, greatly slows down with greater depth.

The board coordinates work like this:

(0,0), (0,1), (0,2)
(1,0), (1,1), (1,2)
(2,0), (2,1), (2,2)
