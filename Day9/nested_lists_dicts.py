capital = {
    "France": "Paris",
    "Brasil": "Brasilia"
}

#Dictionary with list and a dictionary
travel_log = {
    "France": {
        "num_times_visited": 5,
        "cities_visited": ["Lille", "Paris", "Monaco"]
    },
    "countries": capital,
    "Germany": {
        "num_times_visited": 3,
        "cities_visited": ["Stuttgart", "Dortmund", "Monchengladbach",]
    }    
}

# Print Lille
print(travel_log["France"]["cities_visited"][0])

nested_list = ["A", "B", ["C", "D"]]

#Print D
print(nested_list[2][1])

#Print Monchengladbach
print(travel_log["Germany"]["cities_visited"][2])