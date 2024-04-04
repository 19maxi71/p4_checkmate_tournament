

class RoundController:
    
    def __init__(self, round):
        self.round = round
        self.matches = []
        
    def create_round(self):
        name, start_datetime, end_datetime = self.round.get_round_details()
        round = Round(name, start_datetime, end_datetime)
        return round

    # def add_match(self, match):
    #         self.matches.append(match)