

def process_line(line):
    # Split the line using the colon as a separator
    parts = line.strip().split(':')

    # Check if there are two parts
    if len(parts) == 2:
        data = parts[1]
        data = data.strip()
        data_list =  data.split(' ')

        if len(data_list) != 2:
            # If the line doesn't have the expected format, return None
            return None

        return data_list
    else:
        # If the line doesn't have the expected format, return None
        return None

#-------------------------------------------------------------------------

def read_text_file(file_path):
    lineList = []

    with open(file_path, 'r') as file:
        for line in file:
            # Process each line and append the result to the lineList list
            data = process_line(line)
            if data is not None:
                lineList.append(data)

    return lineList

#-------------------------------------------------------------------------

#get ways to beat specific record with specific time
def getWaysToBeat(totalTime,recordTime):
    waysToBeat = 0
    for holdTime in range(1,totalTime+1):
        remainingTime = totalTime -holdTime
        myTime = holdTime * remainingTime
        if myTime > recordTime:
            waysToBeat += 1
    return waysToBeat

#-------------------------------------------------------------------------

def getAnswer(textFile):
    lines = read_text_file(textFile)
    answer = 1
    for race in lines:
        currentRecord = int(race[1])
        currentTime = int(race[0])
        ways = getWaysToBeat(currentTime,currentRecord)
        answer *= ways
    return answer



textFile = "2023\day_six\day_six.txt"
print(getAnswer(textFile))







