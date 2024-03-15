# Rock-Paper-Scissors
Rock Paper Scissors

We maintain a dictionary move_frequencies to keep track of the opponent's move frequencies.
Strategy 1: Counter strategy predicts the opponent's next move based on their previous move. If there is no previous move, it chooses a random move.
Strategy 2: Dynamic strategy counters the opponent's most frequent move.
We choose the next move based on a weighted combination of these strategies. Adjust the weights to optimize performance against different opponents.
