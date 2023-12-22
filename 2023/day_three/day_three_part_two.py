
file_path = '2023\\day_three\\day_three.txt'

with open(file_path) as file:
    lines = file.readlines()
    lines = [line.rstrip() for line in lines]

res = 0

ROW = len(lines)
COL = len(lines[0])

counter = [[0] * COL for _ in range(ROW)]
prods = [[1] * COL for _ in range(ROW)]

for r in range(ROW):
    c = 0
    while c < COL:
        counter_val = 1
        #while iterator is in bounds and the character both current and next character is digit
        while c < COL - 1 and lines[r][c].isdigit() == lines[r][c + 1].isdigit():
            counter_val += 1
            c += 1
        if lines[r][c].isdigit():
            num = int(lines[r][c - counter_val + 1:c + 1])
            valid = False

            #check all squares around number with double for loop
            for x in range(r - 1, r + 2):
                for y in range(c - counter_val, c + 2):
                    if 0 <= x < ROW and 0 <= y < COL and lines[x][y] != "." and not lines[x][y].isdigit():
                        valid = True
                    #if this line is true add to counter and products matrix map
                    if 0 <= x < ROW and 0 <= y < COL and lines[x][y] == "*":
                        counter[x][y] += 1
                        prods[x][y] *= num
                        break
            if valid:
                res += num
        c += 1

gear_ratio = 0

for r in range(ROW):
    for c in range(COL):
        #if counter matrix map has 2 value then add value in product map to gear_ratio
        if counter[r][c] == 2:
            gear_ratio += prods[r][c]

print(res)
print(gear_ratio)

























'''
matrix = []
part_numbers  = []
gear_map = {} #{(row,col): 34}
gear_ratio_numbers = []


with open(file_path, 'r') as file:
    current_line = []
    for line in file:
        for character in line.strip():
            current_line.append(character)
        matrix.append(current_line)
        current_line = []


#dont forget range checks
for row in range(len(matrix)):
    current_num = ''
    counter = 0
    for col in range(len(matrix[row])):
        print(f"row: {row} col: {col}")
        if counter != 0:
            counter -= 1
            continue
        if matrix[row][col].isdigit():
            part_number = False
            gear_number = False
            while counter + col < len(matrix[row]) and matrix[row][col+counter].isdigit():


                #right neighbor
                if col + counter + 1 < len(matrix[row]):
                    if matrix[row][col+counter+1].isdigit() == False and matrix[row][col+counter+1] != ".":
                        part_number = True
                        if matrix[row][col+counter+1] == "*":
                            gear_number = True
                            gear_location = (row, col+counter+1)

                #left neighbor
                if col + counter - 1 > 0:
                    if matrix[row][col+counter-1].isdigit() == False and matrix[row][col+counter-1] != ".":
                        part_number = True
                        if matrix[row][col+counter-1] == "*":
                            gear_number = True
                            gear_location = (row,col+counter-1)

                #bottom neighbor
                if row + 1 < len(matrix):
                    if matrix[row+1][col+counter].isdigit() == False and matrix[row+1][col+counter] != ".":
                        part_number = True
                        if matrix[row+1][col+counter] == "*":
                            gear_number = True
                            gear_location = (row+1,col+counter)

                #top neighbor
                if row - 1 > 0:
                    if matrix[row-1][col+counter].isdigit() == False and matrix[row-1][col+counter] != ".":
                        part_number = True
                        if matrix[row-1][col+counter] == "*":
                            gear_number = True
                            gear_location = (row-1,col+counter)




                #top left
                if row - 1 > 0 and col + counter - 1 > 0:
                    if matrix[row-1][col+counter-1].isdigit() == False and matrix[row-1][col+counter-1] != ".":
                        part_number = True
                        if matrix[row-1][col+counter-1] == "*":
                            gear_number = True
                            gear_location = (row-1,col+counter-1)

                #top right
                if row - 1 > 0 and col + counter + 1 < len(matrix[row]):
                    if matrix[row-1][col+counter+1].isdigit() == False and matrix[row-1][col+counter+1] != ".":
                        part_number = True
                        if matrix[row-1][col+counter+1] == "*":
                            gear_number = True
                            gear_location = (row-1,col+counter+1)

                #bottom left
                if row + 1 < len(matrix) and col + counter - 1 > 0 :
                    if matrix[row+1][col+counter-1].isdigit() == False and matrix[row+1][col+counter-1] != ".":
                        part_number = True
                        if matrix[row+1][col+counter-1] == "*":
                            gear_number = True
                            gear_location = (row+1,col+counter-1)

                
                #bottom right
                if row + 1 < len(matrix) and col + counter + 1 < len(matrix[row]):
                    if matrix[row+1][col+counter+1].isdigit() == False and matrix[row+1][col+counter+1] != ".":
                        part_number = True    
                        if matrix[row+1][col+counter+1] == "*":
                            gear_number = True
                            gear_location = (row+1,col+counter+1)           



                current_num += matrix[row][col+counter]
                counter += 1
            if part_number:
                part_numbers.append(int(current_num))

            if gear_number:
                print(f"found gear number: ")
                if (row,col) not in gear_map:
                    gear_map[(row,col)] = current_num
                    print(f"added number: {current_num} added to: {(row,col)}")
                else:
                    ratio = gear_map[row,col] * current_num
                    gear_ratio_numbers.append(ratio)
                    print("added ratio")


            current_num = ''
            gear_number = False


gear_ratio = 0

for ratio in gear_ratio_numbers:
    gear_ratio += ratio

print(gear_ratio)
print(gear_ratio_numbers)

'''



'''
gear_ratio = 0

for number in part_numbers:
    gear_ratio += number

print(gear_ratio)
print(part_numbers)

'''




