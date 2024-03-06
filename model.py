class Tournament: 
    def __init__(self, name, location, start_date, end_date, num_rounds, description):
        self.name = name
        self.location = location
        self.start_date = start_date
        self.end_date = end_date
        self.num_rounds = num_rounds
        self.current_round = 0
        self.description = description
        self.players = []
        self.rounds = []
    # A voir si on garde cette méthode et si append marche
    def add_player(self, player):
        self.players.append(player)
    
    def generate_pairings(self, players):
        pass
    
    def update_scores(self, round, results):
        pass
    
    def is_tournament_over(self):
        pass


class Round:
    def __init__(self, name, start_datetime, end_datetime):
        self.name = name
        self.start_datetime = start_datetime
        self.end_datetime = end_datetime
        self.matches = []
    
    def add_match(self, match):
        self.matches.append(match)

class Match:
    def __init__(self, player1, player2, score1, score2):
        self.player1 = player1
        self.player2 = player2
        self.score1 = score1
        self.score2 = score2

class Player:
    def __init__(self, name, last_name, date_of_birth, chess_id):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        