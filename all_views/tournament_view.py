def get_tournament_details():
    name = input("Nom du tournoi : ")
    location = input("Lieu : ")
    start_date = input("Date de début : ")
    end_date = input("Date de fin : ")
    num_rounds = int(input("Nombre de rounds : "))
    description = input("Description : ")
    
    return name, location, start_date, end_date, num_rounds, description

# get_tournament_details()