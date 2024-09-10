import os
import sys

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

class ReportView:
    
    @staticmethod
    def display_report_menu():
        """Affiche le menu des rapports et retourne le choix de l'utilisateur."""
        print("1. Générer un rapport des joueurs")
        print("2. Générer un rapport des tournois")
        print("3. Générer un rapport avec le nom et la date de début du tournoi")
        print("4. Générer un rapport des joueurs du tournoi choisi par ordre alphabétique")
        print("5. Générer un rapport sommaire du tournoi")
        return input("Votre choix: ")

    @staticmethod
    def generate_reports(controller):
        """Génère des rapports en fonction du choix de l'utilisateur."""
        choice = ReportView.display_report_menu()
        if choice == "1":
            controller.generate_players_report()
        elif choice == "2":
            controller.generate_tournaments_report()
        elif choice == "3":
            controller.generate_tournament_details_report()
        elif choice == "4":
            controller.generate_tournament_players_report()
        elif choice == "5":
            controller.generate_tournament_summary_report()
        else:
            print("Invalid choice. Please try again.")
        print("Rapport crée dans le dossier all_data")