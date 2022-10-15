# You are a pro MOBA player, you are struggling to become а master of the Challenger tier.
# So, you carefully watch the statistics in the tier.
# You will receive several input lines in one of the following formats:
# "{player} -> {position} -> {skill}"
# "{player} vs {player}"
# The "player" and "position" are strings, and the given "skill" will be an integer number.
# You need to keep track of every player.
# When you receive a player with his position and skill, add him to the players' pool, if he isn`t present, else add his
# position and skill or update his skill, only if the current position skill is lower than the new value.
# If you receive "{player} vs {player}" and both players exist in the tier, they duel with the following rules:
# •	If they got at least one position in common, the player with better total skill points wins and the other is demoted
# from the tier -> remove him.
# •	If they have same total skill points at the same positions, the duel is tie and they both continue in the Season.
# •	If they don`t have positions in common, the duel isn`t happening and both continue in the Season.
# You should end your program when you receive the command "Season end". At that point you should print the players,
# ordered by total skill in descending order, then ordered by player name in ascending order.
# For each player print their position and skill, ordered descending by skill, then ordered by position name in
# ascending order.
# Input / Constraints
# •	The input comes in the form of commands in one of the formats specified above.
# •	Player and position will always be one word string, containing no whitespaces.
# •	Skill will be an integer in the range [0, 1000].
# •	There will be no invalid input lines.
# •	The program ends when you receive the command "Season end".
# Output
# •	The output format for each player is:
# "{player}: {total_skills} skill"
# - {position1} <::> {skill}
# - {position2} <::> {skill}
# …
# - {positionN} <::> {skill}"

def player_update(input_player: str, input_position: str, input_skill: int):
    if input_player not in players:
        players[input_player] = {input_position: input_skill}
    else:
        if input_position not in players[input_player]:
            players[input_player].update({input_position: input_skill})
        else:
            if input_skill > players[input_player][input_position]:
                players[input_player][input_position] = skill
    return players


def duel(input_player_one: str, input_player_two: str):
    if input_player_one in players and input_player_two in players:
        for player_one_skill in players[input_player_one]:
            if player_one_skill in players[input_player_two]:
                if sum(players[input_player_one].values()) > sum(players[input_player_two].values()):
                    del players[input_player_two]
                    break
                elif sum(players[input_player_one].values()) < sum(players[input_player_two].values()):
                    del players[input_player_one]
                    break
    return players


players = {}

command = input()
while command != "Season end":

    if " -> " in command:
        player, position, skill = command.split(" -> ")
        skill = int(skill)
        player_update(player, position, skill)
    elif " vs " in command:
        player_one, player_two = command.split(" vs ")
        duel(player_one, player_two)

    command = input()

players_total_skill = {}
for player in players:
    players_total_skill[player] = sum(players[player].values())

for player, total_skill in sorted(players_total_skill.items(), key=lambda item: (-item[1], item[0])):
    print(f"{player}: {total_skill} skill")
    for position, skill in sorted(players[player].items(), key=lambda item: (-item[1], item[0])):
        print(f"- {position} <::> {skill}")
