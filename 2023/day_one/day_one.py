
#second solution

file_path = '2023\day_one\santa.txt'  
lines_list = []
current = ''
currentLeft = ''
currentRight = ''
numbers_list = []
numMap = ["zero","one","two","three","four","five","six","seven","eight","nine"]
prefixMap = {
            'z':[0],
            'o':[1],
            't':[2,3],
            'f':[4,5],
            's':[6,7],
            'e':[8],
            'n':[9]
            }

def checkLetters(char, line): 
    if char in prefixMap: #if a number starts with current character
        t = 0
        it = 0
        numCounter = 0   
        for number in prefixMap[char]: #for every number that starts with it
            #while were in range of line and characters continue to spell a number
            while index+it < len(line) and numMap[number][t] == line[index + it]: 
                numCounter += 1 
                if numCounter == len(numMap[number]):
                    return str(number)
                t += 1
                it += 1
            #clear values before we move to next number in prefix map
            it = 0 
            t = 0
    return 


#add lines from txt document to list
with open(file_path, 'r') as file:
    for line in file:
        lines_list.append(line.strip())



#find first and last number in each line
for line in lines_list:
    for index, character in enumerate(line):

        #handle alphabetical characters
        if character in prefixMap: #if a number starts with the current character
            letterWord = checkLetters(character, line) #see if it spells a word
            if letterWord != None: #if we found a number from letters
                if currentLeft == '': #if we havent found first number yet add it
                    currentLeft = letterWord
                currentRight = letterWord #update current right everytime we find a number

        #handle numerical characters
        if character.isdigit():  #we have a number
            if currentLeft == '': #if we havent found first number yet add it
                currentLeft = character
            currentRight = character #update current right everytime we find a number
    
    #add to numbers list and reset values
    current = currentLeft + currentRight #concantate two strings 
    numbers_list.append(int(current)) #add the number to the number list as int
    if len(numbers_list) < 5:
        print(f"current line: {line} \n current left: {currentLeft} \n current right: {currentRight} \n current: {current} \n number list: {numbers_list} ")
    current = ''
    currentLeft = ''
    currentRight = ''


#add all numbers in numbers list together for answer
answer = sum(numbers_list)
print(answer)








'''
#first solution

file_path = 'santa.txt'  
lines_list = []
current = ''
currentLeft = ''
currentRight = ''
numbers_list = []


#find first and last number in each line
for line in lines_list:
    for character in line:
        if character.isdigit():  #we have a number
            if currentLeft == '': #if we havent found first number yet add it
                currentLeft = character
            currentRight = character #update current right everytime we find a number
    current = currentLeft + currentRight #concantate two strings 
    numbers_list.append(int(current)) #add the number to the number list as int

    #reset values
    current = ''
    currentLeft = ''
    currentRight = ''

'''