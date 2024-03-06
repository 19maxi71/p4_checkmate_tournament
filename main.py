from view import get_tournament_details
from controller import create_tournament


def main():
    name, location, start_date, end_date, num_rounds, description = get_tournament_details()
    tournament = create_tournament(name, location, start_date, end_date, num_rounds, description)
    print(tournament.name)
    print(tournament.location)
    print(tournament.start_date)
    print(tournament.end_date)
    print(tournament.num_rounds)
    print(tournament.description)
    print(tournament.players)
    print(tournament.rounds)
    print(tournament.current_round)

if __name__ == "__main__":
    main()