class MainView:
    
    def display_main_menu(self):
        """Affiche le menu principal et retourne le choix de l'utilisateur."""
        print("1. Jouer un tournoi")
        print("2. Generer des rapports")
        print("3. Exit")
        return input("Your choice: ")

    def get_file_path(self):
        """Demande à l'utilisateur de saisir le chemin du fichier JSON du tournoi."""
        return input("Enter the path of the tournament JSON file: ")