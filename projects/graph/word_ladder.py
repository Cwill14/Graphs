from util import Queue
'''
Given two words (begin_word and end_word), and a dictionary's word list, return the shortest transformation sequence from begin_word to end_word, such that:
Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that begin_word is not a transformed word.
each transformed word must be the same length
Note: Return None if there is no such transformation sequence.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume begin_word and end_word are non-empty and are not the same.

Sample:
begin_word = "hit"
end_word = "cog"
return: ['hit', 'hot', 'cot', 'cog']
begin_word = "sail"
end_word = "boat"
['sail', 'bail', 'boil', 'boll', 'bolt', 'boat']
beginWord = "hungry"
endWord = "happy"
None
'''

######################################
# 1. TRANSLATE THE PROBLEM INTO GRAPHS TERMINOLOGY
# 2. BUILD YOUR GRAPH
# 3. TRAVERSE YOUR GRAPH
#^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^#
f = open('words.txt', 'r')
words = f.read().split("\n")
f.close()

word_set = set()
for word in words:
    word_set.add(word.lower())

# print(word_set)

def get_neighbors(word):
    # return all words from word_list that are 1 letter different
    neighbors = []
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    string_word = list(word)
    # for each letter in the word
    for i in range(len(string_word)):
        # for each letter in the alphabet
        for letter in alphabet: 
            # change the word letter to the alphabet letter
            list_word = list(string_word)
            list_word[i] = letter
            w = "".join(list_word)
            # if the new word is inthe word_set:
            if w != word and w in word_set:
                # add it to neighbors
                neighbors.append(w)
    return neighbors


def find_ladders(begin, end):
    # create a queue
    q = Queue()
    # enqueue a path to the starting word
    q.enqueue( [begin] )
    # create a visited set
    visited = set()
    # while the queue is not empty
    while q.size() > 0:
        # dequeue the next path
        path = q.dequeue()
        # grab the last word from the path
        v = path[-1]
        # if its's not been visited
        if v not in visited:
            # check if the word is our end word, if so return path
            if v == end:
                return path
            # mark it as visited
            visited.add(v)
            # enqueue a path to each neighbor
            for neighbor in get_neighbors(v):
                path_copy = path.copy()
                path_copy.append(neighbor)
                q.enqueue(path_copy)
            
print(get_neighbors("clark"))
find_ladders("sail", "boat")