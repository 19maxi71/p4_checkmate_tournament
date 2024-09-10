import os
import sys

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)

from all_controllers.tournament_controller import TournamentController
from all_controllers.report_controller import ReportController
from all_views.main_view import MainView

class MainController:

    def __init__(self):
        """Initialise les vues et les contrôleurs."""
        self.main_view = MainView()
        self.tournament_controller = None
        self.report_controller = ReportController()

    def run(self):
        """Boucle principale pour afficher le menu et gérer les choix de l'utilisateur."""
        while True:
            choice = self.main_view.display_main_menu()
            if choice == "1":
                self.create_tournament()
            elif choice == "2":
                self.generate_reports()
            elif choice == "3":
                print("Exiting the program.")
                sys.exit(0)
            else:
                print("Invalid choice. Please try again.")

    def create_tournament(self):
        """Crée un nouveau tournoi et lance les rounds."""
        file_path = os.path.join(os.path.dirname(__file__), 'tournament_data.json')
        self.tournament_controller = TournamentController(file_path)
        self.tournament_controller.run_rounds()

    def load_tournament(self):
        """Charge un tournoi existant et lance les rounds."""
        file_path = self.main_view.get_file_path()
        self.tournament_controller = TournamentController(file_path)
        self.tournament_controller.run_rounds()

    def generate_reports(self):
        """Génère des rapports."""
        self.report_controller.generate_reports()

if __name__ == "__main__":
    controller = MainController()
    controller.run()