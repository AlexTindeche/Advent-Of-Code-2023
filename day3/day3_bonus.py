def is_symbol(symbol_list: list) -> int:
    sym = ''
    for symbol in symbol_list:
        if not symbol.isdigit() and symbol != '.':
            sym = symbol
            break
    return sym

# Open the input file
with open('day3\\day3.txt') as f:
    # Read the inpput file
    input = f.read()
    # print(input)
    # Split the lines by '\n'
    lines = input.split('\n')
    # print(lines)

padded_lines = []
padded_lines.append(['.' for i in range(len(lines[0]) + 2)])
for line in lines:
    padded_lines.append(['.'] + list(line) + ['.'])
padded_lines.append(['.' for i in range(len(lines[0]) + 2)])


for i in range(1, len(padded_lines) - 1):
    for j in range(1, len(padded_lines[i]) - 1):
        padded_lines[i][j] = lines[i - 1][j - 1]

# # Print the padded lines
# for line in padded_lines:
#     print(line)

lines = padded_lines

sum = 0
number = ''
ok = 0
stars = dict()
symbol = None


for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        #print(lines[i][j], end='')
        if lines[i][j].isdigit():
            number += lines[i][j]
            if is_symbol([lines[i][j - 1], lines[i][j + 1], lines[i - 1][j], lines[i + 1][j], lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j - 1], lines[i + 1][j + 1]]) != '':
                if lines[i][j - 1] == '*':
                    symbol = (i, j - 1)
                if lines[i][j + 1] == '*':
                    symbol = (i, j + 1)
                if lines[i - 1][j] == '*':
                    symbol = (i - 1, j)
                if lines[i + 1][j] == '*':
                    symbol = (i + 1, j)
                if lines[i - 1][j - 1] == '*':
                    symbol = (i - 1, j - 1)
                if lines[i - 1][j + 1] == '*':
                    symbol = (i - 1, j + 1)
                if lines[i + 1][j - 1] == '*':
                    symbol = (i + 1, j - 1)
                if lines[i + 1][j + 1] == '*':
                    symbol = (i + 1, j + 1)
                ok = 1
        else:
            if ok == 1:
                if symbol != None:
                    number = int(number)
                    if symbol in stars:
                        stars[symbol].append(number)
                    else:
                        stars[symbol] = [number]
            symbol = None
            number = ''
            ok = 0

product = 1
sum = 0
for key in stars:
    if len(stars[key]) == 2:
        product = stars[key][0] * stars[key][1]
        sum += product
        product = 1


print(sum)



    