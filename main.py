import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
# from all_views.player_view import get_tournament_details
from all_controllers.player_controller import PlayerController

# juste pour test du code        
run_for_test = PlayerController()
test_player = run_for_test.create_player()
run_for_test.save_player(test_player)


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