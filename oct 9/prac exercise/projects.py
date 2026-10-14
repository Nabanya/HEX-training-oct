
import json
#
# projects = [
#     {
#         "project_id": 101,
#         "project_name": "Data Migration",
#         "department": "IT",
#         "budget": 450000,
#         "technologies": ["Python", "SQL", "Azure"],
#         "team": [
#             {
#                 "name": "Vikram",
#                 "role": "Engineer",
#                 "experience": 4
#             },
#             {
#                 "name": "Meera",
#                 "role": "Analyst",
#                 "experience": 3
#             }
#         ]
#     },
#     {
#         "project_id": 102,
#         "project_name": "Customer Analytics",
#         "department": "Analytics",
#         "budget": 300000,
#         "technologies": ["Python", "Pandas", "Power BI"],
#         "team": [
#             {
#                 "name": "Karan",
#                 "role": "Data Analyst",
#                 "experience": 5
#             },
#             {
#                 "name": "Zoya",
#                 "role": "Developer",
#                 "experience": 2
#             }
#         ]
#     },
#     {
#         "project_id": 103,
#         "project_name": "Cloud Modernization",
#         "department": "Cloud",
#         "budget": 600000,
#         "technologies": ["Azure", "Docker", "Python"],
#         "team": [
#             {
#                 "name": "Naveen",
#                 "role": "Cloud Engineer",
#                 "experience": 6
#             },
#             {
#                 "name": "Isha",
#                 "role": "Engineer",
#                 "experience": 4
#             }
#         ]
#     }
# ]
#
# # Write values into projects.json
# with open("projects.json", "w") as file:
#     json.dump(projects, file, indent=4)
#
# print("Project values loaded successfully!")
#
# # Read and display the JSON file
# with open("projects.json", "r") as file:
#     data = json.load(file)
#
# print(data)





# 1
with open("projects.json", "r") as file:
    projects = json.load(file)

print("JSON Data:")
print(projects)

# 2
print("\nDatatype:", type(projects))

# 3
print("\nProject Names:")
for p in projects:
    print(p["project_name"])

# 4
print("\nProjects with Budget Above 400000:")
for p in filter(lambda x: x["budget"] > 400000, projects):
    print(p["project_name"], p["budget"])

# 5
print("\nProjects Using Python:")
for p in filter(lambda x: "Python" in x["technologies"], projects):
    print(p["project_name"])

# 6
total_budget = sum(p["budget"] for p in projects)
print("\nTotal Budget:", total_budget)

# 7
all_technologies = []
for p in projects:
    all_technologies.extend(p["technologies"])

print("\nAll Technologies:")
print(all_technologies)

# 8
unique_technologies = set(all_technologies)
print("\nUnique Technologies:")
print(unique_technologies)

# 9
print("\nAll Team Members:")
for p in projects:
    for member in p["team"]:
        print(
            "Name:", member["name"],
            "Role:", member["role"],
            "Experience:", member["experience"]
        )

# 10
print("\nMembers with More Than 3 Years Experience:")
for p in projects:
    for member in filter(lambda x: x["experience"] > 3, p["team"]):
        print(member["name"], member["experience"])

# 11
total_members = sum(len(p["team"]) for p in projects)
print("\nTotal Team Members:", total_members)

# 12
print("\nProjects Sorted by Budget:")
for p in sorted(projects, key=lambda x: x["budget"], reverse=True):
    print(p["project_name"], p["budget"])

# 13
print("\nProjects Sorted by Name:")
for p in sorted(projects, key=lambda x: x["project_name"]):
    print(p["project_name"])

# 14
print("\nTeam Members Sorted by Experience:")
for p in projects:
    print("\nProject:", p["project_name"])
    sorted_team = sorted(p["team"], key=lambda x: x["experience"])
    for member in sorted_team:
        print(member["name"], member["experience"])
