class Game:
    def __init__(self,name_player,player_scoer):
        self.name=name_player
        self.scoer=player_scoer

    def save(self):
        return checkPoint(self.name,self.scoer) 
    
    def revert(self,revGame): #revert يسترجع
        self.name=revGame.getname()
        self.scoerr=revGame.getscoer()

class checkPoint(Game):
    def __init__(self,name_player,player_scoer):
        super().__init__(name_player,player_scoer)

    def getname(self):
        return self.name
    def getscoer(self):
        return self.scoer
    

class Setdata:
    def __init__(self):
        self.save_data=[]

    def save(self,game):
        self.save.append(game.save())

    def revert(self,game):
        game.revert(self.save.pop()) 

game=Game("Anwar",10)

setdata=Setdata()

setdata.save(game) #save

game.name="EL_Sadat"
game.scoer=20

print("Current State:")
print("Name:", game.name)
print("Score:", game.scoer)