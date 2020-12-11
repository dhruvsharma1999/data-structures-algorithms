#Application for storing high sequence of scores
#Application will present some core data-structuring concepts

class GameEntry:
    """ Represents one entry of a list of high scores"""

    def __init__(self, name, score):
        self._name = name
        self._score = score
    
    def get_name(self):
        #method for returning name
        return self._score

    def get_score(self):
        #method for returning score
        return self._score
    
    def __str__(self):
        #returning string representation of the entry
        return '({0} ,{1}'.format(self._name, self._score)

#Scoarboard class- to add new high score in the list of scoreboard
# Rules:
# 1. only certain amount of high scores are eligibale for eg top 10 high scores
# 2. List is not full so that more high scores can be added
# 3. if list is full and new high score is higher than the last element only then it will be added to the list
# 4. we initially set all entries to NONE

class ScoreBoard:
    """fixed-lenghth sequence of high scores in nondeacreading order"""

    def __init__(self, capacity=10):
        """initialize scoreboard with given maximum capacity
        
        all enteries are none initially
        """
        self._board = [None] * capacity #list of given capacity with empty entries
        self._n = 0  #number of actual entries

        def __init__(self,k):
            """Returns entry at index k"""
            return self._board[k]

        def __str__(self):
            """Returns string representation of the high score list"""
            return '\n'.join(str(self._board[j] for j in range(self._n)))
        
        def add(self, entry):
            """Consider adding entry to high scores"""

            score = entry.get_score()

            #Does new entry qualify as a high score?
            #answer is yes if board is not full or new score is higher than the last entry 
            good = self._n < len(self._board) or score > self._n[-1].get_score()

            if good:
                # no score drops from list ans overall score inscreases
                if self._n < len(self._board):
                    self._n += 1

            j = self._n - 1
            while > 0 and self._board[j-1].get_score() < score:
                self._board[j] = self._board[j-1]
                j -= 1
            self._board[j] = entry 
