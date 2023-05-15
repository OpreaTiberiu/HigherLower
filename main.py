from art import logo, vs
from game_data import data
import random


print(logo)

keep_playing = True

while keep_playing:
    score = 0
    user_won = True

    temp_data = data
    choice_a = random.choice(data)
    data.remove(choice_a)

    while user_won:
        choice_b = random.choice(data)
        data.remove(choice_b)

        print(f"Compare A: {choice_a['name']}, a {choice_a['description']}, from {choice_a['country']}")
        print(vs)
        print(f"Against B: {choice_b['name']}, a {choice_b['description']}, from {choice_b['country']}")
        user_pick = input("Who has more followers? Type 'A' or 'B': ").lower()

        if (user_pick == 'a' and choice_a['follower_count'] >= choice_b['follower_count']) or \
                (user_pick == 'b' and choice_b['follower_count'] >= choice_a['follower_count']):
            score += 1
            print(f"You're right! Current score: {score}")
            choice_a = choice_b
        else:
            print(f"Sorry that is wrong. Final score: {score}")
            score = 0
            user_won = False

    if input("Do you want to try again? Y or N ").lower() == 'n':
        keep_playing = False

