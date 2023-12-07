# Open the input file
with open('day2\day2.txt') as f:
    # Read the inpput file
    input = f.read()
    # Split the lines by '\n'
    games = input.split('\n')
    #print(lines)
    sum = 0
    for game in games:
        product = 1
        # split by ':' to get the game and game data
        game_split = game.split(':')
        # Add the game and game data to the dictionary
        game_id = game_split[0].strip()
        game_data = game_split[1].strip()

        # split the game data by '; ' to get the rounds
        rounds = game_data.split('; ')
        # print(rounds)
        product = 1
        max_green = 0
        max_red = 0
        max_blue = 0
        for round in rounds:
            # split by ', ' to get the round data
            round_split = round.split(', ')
            green = 0
            red = 0
            blue = 0
            for cube in round_split:
                # split by ' ' to get the cube data
                cube = cube.strip()
                cube_split = cube.split(' ')
                # print(cube_split)
                if cube_split[1] == 'green':
                    green += int(cube_split[0])
                elif cube_split[1] == 'red':
                    red += int(cube_split[0])
                elif cube_split[1] == 'blue':
                    blue += int(cube_split[0])

            if red > max_red:
                max_red = red
            if green > max_green:
                max_green = green
            if blue > max_blue:
                max_blue = blue
        
        product = max_red * max_green * max_blue
        sum += product
        
            # print(green, red, blue)
        

print(sum)
    