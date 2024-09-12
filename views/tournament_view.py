import os
import sys

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)


class TournamentView:

    def get_tournament_details(self):
        """Demande les détails du tournoi à l'utilisateur."""
        name = input("Nom du tournoi : ")
        location = input("Lieu : ")
        start_date = input("Date de début : ")
        end_date = input("Date de fin : ")
        total_players = int(input("Nombre de joueurs : ") or 4)
        num_rounds = int(input("Nombre de rounds : ") or 4)
        description = input("Description : ")

        return (
            name,
            location,
            start_date,
            end_date,
            total_players,
            num_rounds,
            description,
        )

    def input_players(self):
        """Demande à l'utilisateur ce qu'il veut faire pour ajouter des joueurs."""
        print(
            "Voulez faire quoi?\n"
            "1. Ajouter un joueur existant\n"
            "2. Ajouter un nouveau joueur\n"
            "3. Charger une liste des joueurs .json"
        )
        choice = input("Votre choix: ")
        return choice

    def prompt_for_action(self):
        """Demande à l'utilisateur s'il veut créer un nouveau tournoi ou charger un tournoi existant."""
        print("1. Créer un nouveau tournoi")
        print("2. Charger un tournoi existant depuis un fichier JSON")
        choice = input("Votre choix: ")
        return choice

    def get_file_path(self):
        """Demande à l'utilisateur de saisir le chemin du fichier JSON du tournoi."""
        return input("Entrez le chemin du fichier JSON du tournoi: ")
