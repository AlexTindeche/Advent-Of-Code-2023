def is_symbol(symbol_list: list) -> int:
    ok = 0
    for symbol in symbol_list:
        if not symbol.isdigit() and symbol != '.':
            ok = 1
            break
    return ok

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
number_is_finished = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[i]) - 1):
        #print(lines[i][j], end='')
        if lines[i][j].isdigit():
            number += lines[i][j]
            if is_symbol([lines[i][j - 1], lines[i][j + 1], lines[i - 1][j], lines[i + 1][j], lines[i - 1][j - 1], lines[i - 1][j + 1], lines[i + 1][j - 1], lines[i + 1][j + 1]]):
                ok = 1
        else:
            if ok == 1:
                #print(number)
                sum += int(number)
            number = ''
            ok = 0

print(sum)



    