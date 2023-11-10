about = {
    "Name" : "Samay", 
    "Age" : "19",
    "Class" : "SECOMP",
    }

print(about)

about["Country"] = "INDIA"

# print(about["Name"])
# print(about["Age"])
# print(about["Class"])
# print(about["Country"])

for things in about:
    print(about[things])
    
#Nesting
travel_log = {
    "France" : {
        "cities_visited" : ["Paris", "Dijon"],
        "Visits" : 12
    },
    "India" : {
        "cities_visited" : ["Mumbai", "Pune"],
        "Visits" : 100
    }
}

# print(travel_log)
# print(travel_log["France"])
# print(travel_log["France"]["cities_visited"])

# print(travel_log["India"]["cities_visited"])
print(travel_log["India"]["Visits"])