class PlayerView:
    def display_player(self, player):
        print(f"Player: {player.name} {player.last_name}")
        print(f"Date of Birth: {player.date_of_birth}")
        print(f"Chess ID: {player.chess_id}")

    def get_player_details(self):
        name = input("Entrer le nom de joueur: ")
        last_name = input("Entrer le prénom de joueur: ")
        date_of_birth = input("Entrer la date de naissance de jouer (YYYY-MM-DD): ")
        chess_id = input("Entrer Identifian National d'Echecs: ")
        return name, last_name, date_of_birth, chess_id
    
get_player_details = PlayerView().get_player_details