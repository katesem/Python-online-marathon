class Gallows:
    
    def __init__(self, words = [], game_over = False):
        self.words = words
        self.game_over = game_over
        
    def play(self, word):      
        if not self.words or (word not in self.words and self.words[-1][-1] == word[0]):
            self.words.append(word)
            return self.words
        else:
            self.game_over = True
            return "game over" 
    
    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"
