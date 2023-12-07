# Open the input file
with open('day2\day2.txt') as f:
    # Read the inpput file
    input = f.read()
    # Split the lines by '\n'
    games = input.split('\n')
    #print(lines)
    sum = 0
    for game in games:
        # split by ':' to get the game and game data
        game_split = game.split(':')
        # Add the game and game data to the dictionary
        game_id = game_split[0].strip()
        game_data = game_split[1].strip()

        # split the game data by '; ' to get the rounds
        rounds = game_data.split('; ')
        # print(rounds)
        ok = 1
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

            if red > 12 or green > 13 or blue > 14:
                # print(game_id)
                ok = 0
        if ok == 1:
            # print(game_id[-1])
            sum += int(game_id.split(' ')[1])
            # print(green, red, blue)


print(sum)
    