# Write a function that takes a boggle board as a 2D array of characters and a word (as a string)
# and returns True if the word appears on the board, else False.

from sets import Set
import copy

def get_neighbors(x,y,n):
    """
    :type x: int
    :type y: int
    "type n: int
    """
    neighbors = []  
    if y > 0:
        neighbors.append((x,y-1))   # up
    if y > 0 and x < n - 1:
        neighbors.append((x+1,y-1)) # up right
    if x < n - 1:
        neighbors.append((x+1,y))   # right
    if x < n - 1 and y < n - 1:
        neighbors.append((x+1,y+1)) # right down
    if y < n - 1:
        neighbors.append((x,y+1))   # down
    if y < n - 1 and x > 0:
        neighbors.append((x-1,y+1)) # down left
    if x > 0:
        neighbors.append((x-1,y))   # left
    if x > 0 and y > 0:
        neighbors.append((x-1,y-1)) # up left
    return neighbors 
    

def find_word(board, word):
    """
    :type board: array
    :type word: string
    """
    if not word:
        return false
    queue = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == word[0]:
                queue.append((1,(i,j),set([(i,j)])))
                keep_going = True
    if keep_going:
        if len(word) == 1:
            return True
        else:
            while queue:
                elt = queue.pop()
                word_index,board_index,visited = elt[0],elt[1],elt[2]
                for neighbor in get_neighbors(board_index[0],board_index[1],len(board[0])):
                    if neighbor not in visited:
                        if board[neighbor[0]][neighbor[1]] == word[word_index]:
                            if word_index + 1 == len(word):
                                return True
                            else:
                                new_visited = copy.deepcopy(visited)
                                new_visited.add(board_index)
                                queue.append((word_index+1,(neighbor[0],neighbor[1]),new_visited))
    return False

# Solution: Loop through the board and find all possible starting places for the word.
# Then perform a BFS-equivalent starting from each possible start, continuing to find
# the next letter in the word and keeping track of what letters have been visited. Time 
# complexity is O(n^2) and space complexity is O(n).
