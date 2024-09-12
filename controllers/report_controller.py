import os
import sys

# Relative path
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

import json
from models.tournament import Tournament
from views.report_view import ReportView
from models.player import Player

class ReportController:

    def __init__(self):
        self.data_folder = os.path.join(os.path.dirname(__file__), "..", "data")

    def generate_reports(self):
        """Génère les rapports en utilisant la vue de rapport."""
        ReportView.generate_reports(self)

    def generate_players_report(self):
        """Génère un rapport HTML de tous les joueurs."""
        players_file = os.path.join(self.data_folder, "players.json")
        with open(players_file, "r") as file:
            players = json.load(file)
        players.sort(key=lambda x: x["last_name"])
        html_content = "<h1>List of All Players</h1><ul>"
        for player in players:
            html_content += f"<li>{player['last_name']} {player['name']} - {player['date_of_birth']} - {player['chess_id']}</li>"
        html_content += "</ul>"
        report_file = os.path.join(self.data_folder, "saved_players_report.html")
        with open(report_file, "w") as file:
            file.write(html_content)

    def generate_tournaments_report(self):
        """Génère un rapport HTML de tous les tournois."""
        tournaments_folder = self.data_folder
        tournaments = [f for f in os.listdir(tournaments_folder) if f.endswith(".json")]
        html_content = "<h1>List of All Tournaments</h1><ul>"
        for tournament in tournaments:
            html_content += f"<li>{tournament}</li>"
        html_content += "</ul>"
        report_file = os.path.join(self.data_folder, "tournaments_report.html")
        with open(report_file, "w") as file:
            file.write(html_content)

    def generate_tournament_details_report(self):
        """Génère un rapport HTML des détails d'un tournoi spécifique."""
        file_path = input("Enter the path of the tournament JSON file: ")
        with open(file_path, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            print("Error: The JSON file contains a list. Expected a dictionary.")
            return

        tournament = Tournament.from_dict(data)
        file_name = os.path.basename(file_path).replace(".json", "")
        html_content = f"<h1>{tournament.name} - {tournament.start_date}</h1>"
        html_content += "<h2>List of Players</h2><ul>"
        players = sorted(tournament.players, key=lambda x: x.name)
        for player in players:
            html_content += f"<li>{player.name}</li>"
        html_content += "</ul>"
        report_file = os.path.join(
            self.data_folder, f"{file_name}_tournament_summary_report.html"
        )
        with open(report_file, "w") as file:
            file.write(html_content)

    def generate_tournament_players_report(self):
        """Génère un rapport HTML des joueurs d'un tournoi spécifique."""
        file_path = input("Enter the path of the tournament JSON file: ")
        with open(file_path, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            print("Error: The JSON file contains a list. Expected a dictionary.")
            return

        tournament = Tournament.from_dict(data)
        file_name = os.path.basename(file_path).replace(".json", "")
        html_content = f"<h1>{tournament.name} - {tournament.start_date}</h1>"
        html_content += "<h2>List of Players (in alphabetical order)</h2><ul>"
        players = sorted(tournament.players, key=lambda x: x.name)
        for player in players:
            html_content += f"<li>{player.last_name} {player.name} - {player.date_of_birth} - {player.chess_id}</li>"
        html_content += "</ul>"
        report_file = os.path.join(
            self.data_folder, f"{file_name}_tournament_players_report.html"
        )
        with open(report_file, "w") as file:
            file.write(html_content)

    def generate_tournament_summary_report(self):
        """Génère un rapport HTML sommaire d'un tournoi spécifique."""
        file_path = input("Enter the path of the tournament JSON file: ")
        with open(file_path, "r") as file:
            data = json.load(file)

        if isinstance(data, list):
            print("Error: The JSON file contains a list. Expected a dictionary.")
            return

        tournament = Tournament.from_dict(data)
        file_name = os.path.basename(file_path).replace(".json", "")
        html_content = f"<h1>{tournament.name} --- START: {tournament.start_date} FIN: {tournament.end_date}</h1>"
        html_content += "<h2>List of Players</h2><ul>"
        players = sorted(tournament.players, key=lambda x: x.name)
        for player in players:
            html_content += f"<li>{player.name} - {player.points} points</li>"
        html_content += "</ul><h2>List of Rounds and Matches</h2>"
        for round in tournament.rounds:
            html_content += f"<h3>{round.name}</h3><ul>"
            for match in round.matches:
                result = match.result if match.result else "No result"
                html_content += f"<li>{match.player1.name} vs {match.player2.name} - Result: {result}</li>"
            html_content += "</ul>"
        report_file = os.path.join(
            self.data_folder, f"{file_name}_tournament_details_report.html"
        )
        with open(report_file, "w") as file:
            file.write(html_content)
