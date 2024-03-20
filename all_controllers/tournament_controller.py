import sys
sys.path.append(r"D:\All OpenClassRooms projects\p4_checkmate_tournament\p4_checkmate_tournament")
import json
from all_models.tournament import Tournament
from all_views.tournament_view import get_tournament_details


# fonction pour créer un tournoi
def create_tournament(name, location, start_date, end_date, num_rounds, description):
    tournament = Tournament(name, location, start_date, end_date, num_rounds, description)
    return tournament