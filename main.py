# Higher or Lower GAME
import random
import art
import game_data
print(art.logo)
game_shld_continue = True
current_score = 0
Compare_a = random.choice(game_data.data)
Compare_b = random.choice(game_data.data)
while game_shld_continue:
    while Compare_a == Compare_b:
        Compare_b = random.choice(game_data.data)
    print(f"A: {Compare_a['name']}, a {Compare_a['description']}, from {Compare_a['country']}")
    print(art.vs)
    print(f"B: {Compare_b['name']}, a {Compare_b['description']}, from {Compare_b['country']}")
    print("\n")
    ans = input("Which has more follower?: Type 'A' or 'B' ").lower()
    if Compare_a["follower_count"] > Compare_b["follower_count"]:
        correct_answer = "a"
    else:
        correct_answer = "b"
    if ans == correct_answer:
        current_score += 1
        print(f"You are right. Current score: {current_score}\n")
        Compare_a = Compare_b
        Compare_b = random.choice(game_data.data)
    else:
        print("Sorry that's wrong.")
        print(f"Final score: {current_score}")
        game_shld_continue = False