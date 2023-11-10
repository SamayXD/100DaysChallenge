import pprint #For printing the DICT in well org manner
import os
os.system('cls' if os.name == 'nt' else 'clear')


#Nesting
travel_log = [
    {
        "Country" : "France",
        "cities_visited" : ["Paris", "Dijon"],
        "Visits" : 12
    },
    {
        "Country" : "India",
        "cities_visited" : ["Mumbai", "Pune"],
        "Visits" : 100
    }
]

country = ""
cities_visited = []
Visits = 0


def add_log():
    print("Add Country: ")
    country = input()
    
    print("Add cities_visited: ")
    cities_visited = input()
    
    print("Add Visits: ")
    Visits = int(input())
    
    travel_log.append(
        {
            "Country" : country, 
            "cities_visited" : cities_visited, 
            "Visits" : Visits
        }
    )
    
add_log()

pprint.pprint(travel_log[1]["Country"])
os.system('cls' if os.name == 'nt' else 'clear')
print("Current Travel LOG")
for i in range(0, len(travel_log)):
    # print(travel_log[i]["Country"])
    print()

    print("{} => {}".format("Country", travel_log[i]["Country"]))
    print("{} => {}".format("Cities", travel_log[i]["cities_visited"]))
    print("{} => {}".format("Visits", travel_log[i]["Visits"]))

input()