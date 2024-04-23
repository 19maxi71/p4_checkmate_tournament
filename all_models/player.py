# import os
import json
import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
from all_views.player_view import PlayerView

class Player:
    def __init__(self, name, last_name, date_of_birth, chess_id):
        self.name = name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.chess_id = chess_id
        # Ajout automatique du joueur dans la liste des joueurs players.json
        self.save_player(self.serialized_player())
    
    # fonction pour afficher les données d'un joueur sous forme de string. à supp si pas besoin
    def __repr__(self):
        return f"{self.name} {self.last_name} {self.date_of_birth} {self.chess_id}"
    
    # fonction pour sérialiser les données d'un joueur. mettre les données dans un dictionnaire pour json
    # @staticmethod
    def serialized_player(self):
        serialized_player_data = {
            "name": self.name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "chess_id": self.chess_id
        }
        return serialized_player_data
        
    @staticmethod
    def save_player(player_data):
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            data = []

        data.append(player_data)

        with open('players.json', 'w') as file:
            json.dump(data, file)
      
      
    # methode pour chercher un joueur dans la liste des joueurs.
    @staticmethod
    def player_exists(player_data):
        # print("player_exists marche bien") # pour voir si la fonction est bien appelée
        try:
            with open(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament\all_data\players.json", 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("ouvre pas ton json machine")  # voir si l'erreur est là
            return False

        # print(f"data: {data}")  # print pour checker si on a bien les données des joueurs
        # print(f"player_data: {player_data}")  # print pour checker si on a bien les données du joueur à chercher

        for player in data:
            if player['chess_id'] == player_data['chess_id']:
                print(f"Joueur trouvé: {player['name']} {player['last_name']}")
                return player

        print(f"Joueur non trouvé.")
        return False

    # def __dict__(self):
    #     return {
    #         "name": self.name,
    #         "last_name": self.last_name,
    #         "date_of_birth": self.date_of_birth,
    #         "chess_id": self.chess_id
    #     }

    @staticmethod
    def load_players_from_file(file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            print("Chemin du fichier non valide.")
            return []
        return data