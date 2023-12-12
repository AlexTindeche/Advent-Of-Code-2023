# Open the input file
with open('day4.txt') as f:
    # Read the inpput file
    input = f.read()
    # print(input)
    # Split the lines by '\n'
    lines = input.split('\n')
    # print(lines)
sum = 0
num_of_wining_numbers = 0
cards = dict()
for line in lines:
    split_line = line.split(': ')
    card_number = int(split_line[0].split(' ')[-1])
    split_line = split_line[1].strip().split(' | ')
    # print(split_line)
    wining_numbers = [int(num.strip()) for num in split_line[0].split(' ') if num != '']
    # print(wining_numbers)
    my_numbers = [int(num.strip()) for num in split_line[1].split(' ') if num != '']
    # print(my_numbers)
    cards[card_number] = [wining_numbers, my_numbers]

copies_of_cards = []

for card in cards:
    num_of_wining_numbers = 0
    for number in cards[card][0]:
        if number in cards[card][1]:
            num_of_wining_numbers += 1
    if num_of_wining_numbers != 0:
        for num in range(card + 1, card + num_of_wining_numbers + 1):
            copies_of_cards.append(num)
i = 0
while i < len(copies_of_cards):
    num_of_wining_numbers = 0
    for wining_numbers in cards[copies_of_cards[i]][0]:
        if wining_numbers in cards[copies_of_cards[i]][1]:
            num_of_wining_numbers += 1
    if num_of_wining_numbers != 0:
        for num in range(copies_of_cards[i] + 1, copies_of_cards[i] + num_of_wining_numbers + 1):
            copies_of_cards.append(num)
    i += 1
        
print(len(copies_of_cards) + len(cards))



    