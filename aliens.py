# We're going to create a user designed alien and amount.

# Empty list for storing out aliens
aliens = []


# Make the aliens from user input!!
def alienSetup():
    while  True:
        try:
            alienSetup.alienTotal = int(input('How many aliens would you like to create?: '))
            print(
                f"Now that we're going to create {alienSetup.alienTotal} aliens, we need some extra info about them...")
        except ValueError:
            print('Sorry, please try again...')
        else:
            break

    alienSetup.alien_c = input(
        'Which of these colors should the alien be?\n(green, blue, orange, red, purple, chrome):')
    alienSetup.availColors = ['green', 'blue', 'orange', 'red', 'purple', 'chrome']
    while alienSetup.alien_c.lower() not in alienSetup.availColors:
        print(
            f"{alienSetup.alien_c.lower()} is not a valid option, please try again...\n(green, blue, orange, red, purple, chrome):")
        alienSetup.alien_c = input().lower()

    while True:
        try:
            alienSetup.alien_speed = int(input('How fast should the aliens be?: '))
            print(f'These aliens will now be set to have a speed of {alienSetup.alien_speed}')
        except ValueError:
            print('Sorry, please try again...')
        else:
            break

    while True:
        try:
            alienSetup.alien_point = int(
                input(f'How many points should each of these {alienSetup.alienTotal} aliens be worth?'))
            print(f'These aliens will now be worth {alienSetup.alien_point} point(s).')
        except ValueError:
            print('Sorry, please try again...')
        else:
            break
    return alienSetup.alienTotal, alienSetup.alien_point, alienSetup.alien_speed, alienSetup.alien_c


def alienDict(tota, poia, spea, cola):
    # Get and set the alien attributes
    for alien_number in range(alienSetup.alienTotal):
        alienDict.alien = {}
        alienDict.alien['points'] = alienSetup.alien_point
        alienDict.alien['speed'] = alienSetup.alien_speed
        alienDict.alien['color'] = alienSetup.alien_c
        # Here we get and set the color key and value for our alien dicts
        aliens.append(alienDict.alien)


# print(f'Each new alien will be {alien[]} and move at a speed of {alien_speed} while being worth {alien_point} point(s) each.')

while True:
    try:
        createAliens = input('Would you like to generate some aliens?(y/n): ')
        if createAliens != 'y' or 'n':
            createAliens = input('Please enter y or n...: ')
        else:
            break
        atot, apoi, aspe, acol = alienSetup()
        alienDict(atot, apoi, aspe, acol)
        print(aliens)
    except ValueError:
        print('Sorry, please try again...')
    else:
        break
