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
        for c in line:
            if c.isdigit():
                if first_int == -1:
                    first_int = c
                    last_int = c
                else:
                    last_int = c
        number = int(str(first_int) + str(last_int))
        sum += number

print(sum)