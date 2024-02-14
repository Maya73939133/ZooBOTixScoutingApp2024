import json

team_number = int(input("Enter a team number: "))
eventfile = open('./2024mibat.json')
readfile = json.loads(eventfile.read())

def getindexofteam(team_num):
    for i in range(0, len(readfile) - 1):
        dictionary = readfile[i]
        if dictionary.get("team_number") == team_num:
            index = i
            return index
            break

indexx = getindexofteam(team_number)

try:
    team = readfile[indexx]  
    print(team.get("nickname") + "\n" + team.get("city") + " " + team.get("postal_code") + ", " + team.get("state_prov"))
except TypeError:
    print("\033[0;31mERROR! INVALID TEAM NUMBER\033[0;m")  