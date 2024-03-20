class Player:
    def __init__(self, name, last_name, date_of_birth, chess_id):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
    
    # # fonction pour afficher les données d'un joueur sous forme de string. à supp si pas besoin
    # def __repr__(self):
    #     return f"{self.name} {self.last_name}"
    
    # fonction pour sérialiser les données d'un joueur. mettre les données dans un dictionnaire pour json
    def serialized_player(self):
        return serialized_player_data = {
            "name": self.name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "chess_id": self.chess_id
        }
    
    # def save_player(player_data):
    #     try:
    #         with open('players.json', 'r') as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         data = []

    #     data.append(player_data)

    #     with open('players.json', 'w') as file:
    #         json.dump(data, file)
            
    # def player_exists(player_data):
    #     try:
    #         with open('players.json', 'r') as file:
    #             data = json.load(file)
    #     except (FileNotFoundError, json.JSONDecodeError):
    #         return False

    #     for player in data:
    #         if player['name'] == player_data['name'] and player['last_name'] == player_data['last_name']:
    #             return True

    #     return False
