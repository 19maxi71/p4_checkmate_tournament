from all_models.player import Tournament, Round, Match, Player

# fonction pour créer un tournoi
def create_tournament(name, location, start_date, end_date, num_rounds, description):
    tournament = Tournament(name, location, start_date, end_date, num_rounds, description)
    return tournament
# fonction pour créer un tour
def create_round(name, start_datetime, end_datetime):
    round = Round(name, start_datetime, end_datetime)
    return round
# fonction pour créer un match
def create_match(player1, player2, score1, score2):
    match = Match(player1, player2, score1, score2)
    return match
# fonction pour créer un joueur
def create_player(name, last_name, date_of_birth, chess_id):
    player = Player(name, last_name, date_of_birth, chess_id)
    return player