class MainView:
    
    def display_main_menu(self):
        print("1. Jouer un tournoi")
        print("2. Generer des rapports")
        print("3. Exit")
        return input("Your choice: ")

    def get_file_path(self):
        return input("Enter the path of the tournament JSON file: ")