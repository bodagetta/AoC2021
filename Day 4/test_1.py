from typing import final


with open('input.txt') as f:
    lines = f.readlines()

bingo_numbers = lines[0].strip('\n').split(',')
number_of_cards = (len(lines) - 1)/6
cards = []
winning_card_index = []

print("Bingo Numbers: ", bingo_numbers)

print("Number of Cards: ", number_of_cards)


def prep_line(line):
    line = line.strip('\n')
    line = line.split()
    return line


def build_single_card_array(start_index):
    card = []
    columns = []
    column1 = []
    column2 = []
    column3 = []
    column4 = []
    column5 = []
    for count in range(0, 5):
        card.append(prep_line(lines[start_index+count]))

    for row in card:
        column1.append(row[0])
        column2.append(row[1])
        column3.append(row[2])
        column4.append(row[3])
        column5.append(row[4])
    card.append(column1)
    card.append(column2)
    card.append(column3)
    card.append(column4)
    card.append(column5)

    return card


def check_row_for_win(row):
    for element in row:
        if not element.startswith('*'):
            return False

    return True


def check_cards_for_number(cards, number):
    card_return = []
    cards_return = []
    for card in cards:
        card_return = []
        for row in card:
            row = ["*"+x if x == number else x for x in row]
            # print(number)
            # print(row)
            card_return.append(row)
            # if element == number:
            #     print(element)
        cards_return.append(card_return)
    return cards_return

def calculate_winning_score(card):
    card_score = 0
    for index in range(0,5):
        row_score = card[index]
        for element in row_score:
            if not element.startswith('*'):
                card_score += int(element)
                # print("Card Score: ", card_score)
                # print("Row Score: ", row_score)
    final_score = card_score * int(number)
    print("Final Score: ", final_score)
    print("-----")


for index in range(2, (int(number_of_cards)*5+2), 6):
    cards.append(build_single_card_array(index))

for number in bingo_numbers:
    cards = check_cards_for_number(cards, number)
    for idx, card in enumerate(cards):
        if idx in winning_card_index:
            continue
        for row in card:
            if check_row_for_win(row):
                print("Winning Number: ", number)
                print("Winning Row: ", row)
                print("Winning Card #", (idx+1))
                # calculate Score for winning board, sum of all unmarked numbers
                # only first five rows matter, last 5 rows are columns and duplicates
                calculate_winning_score(card)
                # cards.remove(card)
                if idx not in winning_card_index:
                    winning_card_index.append(idx)
                break

# print(winning_card_index[-1])
# print(cards[winning_card_index[-1]])
calculate_winning_score(cards[winning_card_index[-1]])