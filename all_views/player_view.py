class PlayerView:
    
    
    def get_player_details(self):
        name = input("Entrer le nom de joueur: ")
        last_name = input("Entrer le prénom de joueur: ")
        date_of_birth = input("Entrer la date de naissance de jouer (YYYY-MM-DD): ")
        chess_id = input("Entrer Identifian National d'Echecs: ")
        return name, last_name, date_of_birth, chess_id
    
    def get_player_chess_id(self):
        chess_id = input("Entrer votre Identifiant National d'Echecs: ")
        return str(chess_id)