
file_path = '2023\day_three\day_three.txt'

matrix = []
part_numbers  = []

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
        if counter != 0:
            counter -= 1
            continue
        if matrix[row][col].isdigit():
            part_number = False
            while counter + col < len(matrix[row]) and matrix[row][col+counter].isdigit():

                #right neighbor
                if col + counter + 1 < len(matrix[row]):
                    if matrix[row][col+counter+1].isdigit() == False and matrix[row][col+counter+1] != ".":
                        part_number = True

                #left neighbor
                if col + counter - 1 > 0:
                    if matrix[row][col+counter-1].isdigit() == False and matrix[row][col+counter-1] != ".":
                        part_number = True

                #bottom neighbor
                if row + 1 < len(matrix):
                    if matrix[row+1][col+counter].isdigit() == False and matrix[row+1][col+counter] != ".":
                        part_number = True

                #top neighbor
                if row - 1 > 0:
                    if matrix[row-1][col+counter].isdigit() == False and matrix[row-1][col+counter] != ".":
                        part_number = True





                #top left
                if row - 1 > 0 and col + counter - 1 > 0:
                    if matrix[row-1][col+counter-1].isdigit() == False and matrix[row-1][col+counter-1] != ".":
                        part_number = True
                #top right
                if row - 1 > 0 and col + counter + 1 < len(matrix[row]):
                    if matrix[row-1][col+counter+1].isdigit() == False and matrix[row-1][col+counter+1] != ".":
                        part_number = True
                
                #bottom left
                if row + 1 < len(matrix) and col + counter - 1 > 0 :
                    if matrix[row+1][col+counter-1].isdigit() == False and matrix[row+1][col+counter-1] != ".":
                        part_number = True
                
                #bottom right
                if row + 1 < len(matrix) and col + counter + 1 < len(matrix[row]):
                    if matrix[row+1][col+counter+1].isdigit() == False and matrix[row+1][col+counter+1] != ".":
                        part_number = True               


                current_num += matrix[row][col+counter]
                counter += 1
            if part_number:
                part_numbers.append(int(current_num))
            current_num = ''

answer = 0

for number in part_numbers:
    answer += number

print(answer)
print(part_numbers)







