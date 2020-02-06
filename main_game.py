import player_stats

print("""You are a scout in the Royal Army for the king. You've just
recieved intel and need to quickly deliever the message. Do you accept
the challenge? (enter Y/N [case sensitive])""")

starting_choice = input("> ")

if starting_choice == 'Y':

    start_game = player_stats.creation()

    start_game.customize()

else:
    exit()

print('tesdsfres')
