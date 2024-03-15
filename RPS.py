import random

def player(prev_play, opponent_history=[]):
    move_frequencies = {"R": 0, "P": 0, "S": 0}
    for play in opponent_history:
        move_frequencies[play] += 1
      
    if prev_play:
        predicted_move = {"R": "P", "P": "S", "S": "R"}[prev_play]
      
    else:
        predicted_move = random.choice(["R", "P", "S"])
      
    most_frequent_move = max(move_frequencies, key=move_frequencies.get)
    dynamic_move = {"R": "P", "P": "S", "S": "R"}[most_frequent_move]
    weighted_choice = random.choices([predicted_move, dynamic_move], weights=[0.6, 0.4])[0]
    return weighted_choice
