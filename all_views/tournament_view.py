class TournamentView:
    
    
    def get_tournament_details(self):
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début : ")
        end_date = input("Date de fin : ")
        total_players = int(input("Nombre de joueurs : ") or 4)
        num_rounds = int(input("Nombre de rounds : ") or 4)
        description = input("Description : ")
        
        return name, location, start_date, end_date, total_players, num_rounds, description

    def input_players(self):
        print("Voulez faire quoi?\n"
              "1. Ajouter un joueur existant\n"
              "2. Ajouter un nouveau joueur\n"
              "3. Charger une liste des jouers .json")
        choice = input("Votre choix: ")
        return choice
    # print(get_tournament_details())


# # instance de TournamentView
# tournament_view = TournamentView()

# # appel input_players methode
# choice = tournament_view.input_players()

# # Print choice
# print(choice)