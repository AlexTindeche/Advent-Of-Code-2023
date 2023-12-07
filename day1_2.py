# Defining the numbers
numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

# Open the input file
with open('day1.txt') as f:
    # Read the inpput file
    input = f.read()
    # Split the lines by '\n'
    lines = input.split('\n')
    #print(lines)
    sum = 0
    for line in lines:
        first_int = -1
        last_int = -1
        for i in range(len(line)):
            if line[i].isdigit():
                if first_int == -1:
                    first_int = line[i]
                    last_int = line[i]
                else:
                    last_int = line[i]
            else:
                # We verify if starting with this character, there is spelled a number
                for number in numbers:
                    # print(line[line.index(line[i]):min(line.index(line[i]) + len(number), len(line))] + ' ' + number, end=' ')
                    if line[i:min(i + len(number), len(line))] == number:
                        if first_int == -1:
                            first_int = numbers.index(number) + 1
                            last_int = numbers.index(number) + 1
                        else:
                            last_int = numbers.index(number) + 1
                    # print(first_int, last_int)
        # print(str(first_int) + str(last_int))
        number = int(str(first_int) + str(last_int))
        sum += number

print(sum)