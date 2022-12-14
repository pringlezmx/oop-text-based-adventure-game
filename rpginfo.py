class RPGInfo():
    
    author = "Anonymous"
    
    def __init__(self, game_title):
        self.title = game_title
        
    
    def welcome(self):
        print("welcome to" + self.title)
        
    @staticmethod
    def info():
        print("made using the OOP RPG creater")
        
    
    @classmethod
    def credit(cls):
        print ("thank you for playing")
        print("created by " + cls.author)