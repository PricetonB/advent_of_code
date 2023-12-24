

def process_line(line):
    # Split the line using the colon as a separator
    parts = line.strip().split(':')

    # Check if there are two parts
    if len(parts) == 2:
        numbers = parts[1]

        # Split the right side using the '|' character
        left_numbers = list(map(int, numbers.split('|')[0].split()))
        right_numbers = list(map(int, numbers.split('|')[1].split()))


        # Return the result as a list containing one list of numbers
        return [left_numbers,right_numbers]
    else:
        # If the line doesn't have the expected format, return None
        return None

def read_text_file(file_path):
    cards = []

    with open(file_path, 'r') as file:
        for line in file:
            # Process each line and append the result to the cards list
            card = process_line(line)
            if card is not None:
                cards.append(card)

    return cards




# Example usage
file_path = '2023\day_four\day_four.txt'  # Replace with the actual path to your text file
card_list = read_text_file(file_path)

answer = 0
for card in card_list:
    wins_on_card = 0
    player_numbers = card[1]
    winning_numbers = card[0]
    for player_number in player_numbers:
        if player_number in winning_numbers:
            wins_on_card += 1
    if wins_on_card == 1:
        answer += 1
    if wins_on_card > 1:
        answer += (2**(wins_on_card-1))


print(answer)