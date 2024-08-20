import smtplib, ssl
from random import choice
team_list = ["Berry", "Air Panther", "_Deadringer_", "Deeqks Freaks", "Amobob amadeo", 
             "Philly Special", "Go Crawford", "BRs Ballers", "El Borrachero",
             "#A", "Bill Bixsby HULK", "Bird Brains"]
team_list_draft_pos = []
team_index_rando = []
draft_result = []
temp_team_list = []
final_team_list = []
draft_order = []


z = 1
while z < 13:
    curSlot = choice([i for i in range (1,13) if i not in team_list_draft_pos])
    team_list_draft_pos.append(curSlot)
    draft_result.append(str(curSlot))
    z = z + 1

z=1
while z < 13:
    curTeam = choice([i for i in range (0,12) if i not in team_index_rando])
    team_index_rando.append(curTeam)
    z = z + 1

counter = 0
while len(team_index_rando) > 0:
    counter = counter + 1
    work =  team_index_rando.pop()
    temp_team_list.append(team_list[work])

traverseC = 0
while traverseC < 12:
    cTeam = temp_team_list[traverseC] + ":"
    cSlot = draft_result[traverseC]
    cVal = cTeam+cSlot
    final_team_list.append(cVal)
    traverseC = traverseC + 1
    
finalC = 0
while finalC < 13:
    for curVal in final_team_list:
        curData = curVal.split(':')
        if curData[1] == str(finalC):
            draft_order.append(curData[0])
    finalC = finalC + 1

    
for teamN in draft_order:
    print teamN

