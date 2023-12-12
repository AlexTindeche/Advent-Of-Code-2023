# Open the input file
with open('day4\\day4.txt') as f:
    # Read the inpput file
    input = f.read()
    # print(input)
    # Split the lines by '\n'
    lines = input.split('\n')
    # print(lines)
sum = 0
num_of_wining_numbers = 0
for line in lines:
    split_line = line.split(': ')
    split_line = split_line[1].strip().split(' | ')
    wining_numbers = [num.strip() for num in split_line[0].split(' ')]
    # print(wining_numbers)
    my_numbers = [num.strip() for num in split_line[1].split(' ') if num != '']
    # print(my_numbers)

    for wining_number in wining_numbers:
        if wining_number in my_numbers:
            num_of_wining_numbers += 1

    if num_of_wining_numbers != 0:
        sum += 2 ** (num_of_wining_numbers - 1)
    num_of_wining_numbers = 0

print(sum)



    