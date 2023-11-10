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