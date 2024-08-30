import sys
import os
# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

# from all_views.player_view import get_tournament_details
from all_controllers.player_controller import PlayerController

# juste pour test du code        
run_for_test = PlayerController()

while True:
    test_player = run_for_test.create_player()
    run_for_test.save_player(test_player)
    
    add_another = input("Voulez ajouter encore un joueur? (y/n): ")
    # lower contre majuscule
    if add_another.lower() != 'y':
        break


# def main():
#     name, location, start_date, end_date, num_rounds, description = get_tournament_details()
#     tournament = create_tournament(name, location, start_date, end_date, num_rounds, description)
#     print(tournament.name)
#     print(tournament.location)
#     print(tournament.start_date)
#     print(tournament.end_date)
#     print(tournament.num_rounds)
#     print(tournament.description)
#     print(tournament.players)
#     print(tournament.rounds)
#     print(tournament.current_round)

# idiome pour lancer le script
# if __name__ == "__main__":
#     main()