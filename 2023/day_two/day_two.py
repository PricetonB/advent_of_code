

#Game 1... = inputDays[1]

inputDays = [] #list of days ex. ['4 blue; 1 green, 2 red; 4 blue, 1 green, 6 red','4 blue; 1 green, 2 red; 4 blue']
listOfDayKeys = [] # contains max num for each color for each day ex. [{'green':2 , "red":9 , "blue":3},{'green':5 , "red":2 , "blue":1},] 

def parse_games(line):
    # Split the line by semicolons to get individual games
    games = line.split(";")
    
    # Process each game
    game_info = {'green':0 , "red":0 , "blue":0}
    for game in games:
        # Split each game by commas to get colors and quantities
        items = game.split(",")
        
        # Extract color and  max quantity for each item

        for item in items:
            parts = item.strip().split(" ")
            quantity = int(parts[0])
            color = parts[1].strip()
            game_info[color] = max(game_info[color],quantity)
        
    return game_info

def getAnswer(dkl):
#pass in a list of day keys and check each color in hashmap {'green':0 , "red":0 , "blue":0}
#check each color if its over max add to total
    total = 0
    for numToAdd, key in enumerate(dkl):
        if key["red"] > 12:
            continue
        if key["green"] > 13:
            continue
        if key["blue"] > 14:
            continue
        total += numToAdd
    return total


# CREATE INPUT DAYS LIST
with open('2023\day_two\day_two.txt', 'r') as file:
    # Read all lines from the file
    lines = file.readlines()
# Iterate through each line, excluding the first 6 characters, and add to the list
for line in lines:
    inputDays.append(line[8:].strip())  # Exclude the first 6 characters and strip any leading/trailing whitespace



# CREATE DAY KEY LIST
for day in inputDays:
    dayKey = parse_games(day)
    listOfDayKeys.append(dayKey)



#GET ANSWER
answer = getAnswer(listOfDayKeys)
print(answer)


