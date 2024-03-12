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
    # A voir avec Driss ce qu'il y a définir comme fonctions. ET si on garde cette méthode
    def generate_pairings(self, players):
        pass
    
    def update_scores(self, round, results):
        pass
    
    def is_tournament_over(self):
        pass