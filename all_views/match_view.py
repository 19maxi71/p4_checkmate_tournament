import sys
import os

# Chemin relatif
current_dir = os.path.dirname(__file__)
project_dir = os.path.dirname(current_dir)
sys.path.append(project_dir)


class MatchView:

    def input_match_result(self, match):
        """Demande à l'utilisateur d'entrer le résultat du match."""
        print(f" >>> Match entre {match.player1.name} et {match.player2.name} <<<")
        while True:
            result = input(
                "Entrer le résultat du match (1 pour victoire de joueur 1, 2 pour victoire de joueur 2, 0 pour match nul): "
            )
            if result in ["1", "2", "0"]:
                return result
            else:
                print("Valeur incorrecte. Veuillez entrer 1, 2 ou 0.")

    def display_match_result(self, match):
        """Affiche le résultat du match."""
        if match.result == "1":
            print(
                f"{match.player1.name} a gagné le match \n"
                f"{match.player1.name} obtient {match.player1.points} points \n"
                f"et {match.player2.name} obtient {match.player2.points} points"
            )
        elif match.result == "2":
            print(
                f"{match.player2.name} a gagné le match \n"
                f"{match.player2.name} obtient {match.player2.points} points \n"
                f"et {match.player1.name} obtient {match.player1.points} points"
            )
        elif match.result == "0":
            print(
                f"Match nul, {match.player1.name} et {match.player2.name} obtiennent chacun 0.5 points"
            )
