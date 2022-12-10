alphabet=[*"abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"]
file_contents = open("days/03/input.txt").read()
knapsacks = file_contents.split("\n")

total_sum = 0

group_common_chars = False
group_sum = 0

for index in range(len(knapsacks)):
  if (index != 0 and index % 3 == 0):
    for char in group_common_chars:
      group_sum += alphabet.index(char) + 1
    group_common_chars = False

  knapsack = knapsacks[index]

  if (group_common_chars == False):
    group_common_chars = set((knapsack))
  else:
    group_common_chars = group_common_chars.intersection(set((knapsack)))
  
  halfway_point = int(len(knapsack) / 2)
  first_half = set((knapsack[:halfway_point]))
  second_half = set((knapsack[halfway_point:]))
  common_chars = first_half.intersection(second_half)

  for char in common_chars:
    total_sum += alphabet.index(char) + 1
  
print("Part 1: " + str(total_sum))
print("Part 2: " + str(group_sum))