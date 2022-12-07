legend_op = {
  "A": "Rock",
  "B": "Paper",
  "C": "Scissors"
}

legend_response = {
  "X": "Rock",
  "Y": "Paper",
  "Z": "Scissors"
}

legend_wins = {
  "A": "B",
  "B": "C",
  "C": "A"
}

legend_weights = {
  "Rock": 1,
  "Paper": 2,
  "Scissors": 3
}

def determine_selection_points(response):
  return legend_weights[response]

def determine_game_points(op, response):
  if (op == response):
    return 3
  if ((op == "Scissors" and response == "Paper") or (op == "Paper" and response == "Rock") or (op == "Rock" and response == "Scissors")):
    return 0
  return 6

def find_move_based_on_input(op, my_play):
  if (my_play == "X"):
    #we need to lose
    return legend_wins[legend_wins[op]]
  elif (my_play == "Y"):
    #we need to draw
    return op
  else:
    #we need to win
    return legend_wins[op]


file_contents = open("days/02/input.txt").read()
rounds = file_contents.split("\n")

p1_total = 0
p2_total = 0
for game_round in rounds:
  round_inputs = game_round.split(" ")
  op = round_inputs[0]
  my_play = round_inputs[1]
  # get optimal move based on my_play
  my_move = find_move_based_on_input(op, my_play)
  # calculate score based on optimal move
  formatted_op = legend_op[op]
  formatted_response = legend_op[my_move]
  my_round_points = determine_game_points(formatted_op, formatted_response)
  my_selection_points = determine_selection_points(formatted_response)
  p2_total += my_round_points + my_selection_points
  my_round_points = determine_game_points(formatted_op, legend_response[my_play])
  my_selection_points = determine_selection_points(legend_response[my_play])
  p1_total += my_round_points + my_selection_points


print("Part 1: " + str(p1_total))
print("Part 2: " + str(p2_total))
  
