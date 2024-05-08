class Player:
    def __init__(self, mission="", weapon=""):
        self.mission = mission
        self.weapon = weapon

    def render(self):
        pass

class RedTeamPlayer(Player):
    def __init__(self):
        super().__init__("Capture Red Flag")

    def render(self):
        print(f"{self.weapon} and {self.mission}")

class BlueTeamPlayer(Player):
    def __init__(self):
        super().__init__("Capture Blue Flag")

    def render(self):
        print(f"{self.weapon} and {self.mission}")

class PlayerFactory:
    @staticmethod
    def get_player(type):
        if type == "RedTeam":
            return RedTeamPlayer()
        elif type == "BlueTeam":
            return BlueTeamPlayer()
        else:
            print("Team not Available")
            raise ValueError("Team not Available")

# استخدم الكود التالي لاختبار الكود المحول
# player_factory = PlayerFactory()
# player1 = player_factory.get_player("RedTeam")
# player2 = player_factory.get_player("BlueTeam")
# player1.render()
# player2.render()
