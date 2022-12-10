import re

file_contents = open("days/05/input.txt").read()
initial_state, moves = file_contents.split("\n\n")

stacks_p1 = [
  [],[],[],
  [],[],[],
  [],[],[]
]
stacks_p2 = [
  [],[],[],
  [],[],[],
  [],[],[]
]
stacks = [(stacks_p1, False), (stacks_p2, True)]
slice_size = 4
for line in initial_state.split("\n"):
  pos = 0
  stack_index = 0
  while pos < len(line):
    current_slice = line[pos:pos+slice_size]
    if (current_slice.strip() != ""):
      for stack, _ in stacks:
        stack[stack_index].insert(0, current_slice.strip())
    pos+=slice_size
    stack_index += 1

for move in moves.split("\n"):
  if move == "":
    continue
  pattern = re.compile(r"^move\s(?P<count>.*?)\sfrom\s(?P<from_stack>.*?)\sto\s(?P<to_stack>.*?)$", re.VERBOSE)
  match = pattern.match(move)
  count = int(match.group("count"))
  from_stack = int(match.group("from_stack")) - 1
  to_stack = int(match.group("to_stack")) - 1

  for stack, can_handle_multiple in stacks:
      idx_to_slice_from = len(stack[from_stack]) - count
      slice_to_move = stack[from_stack][idx_to_slice_from:]
      if (not can_handle_multiple):
        slice_to_move.reverse()
      stack[to_stack].extend(slice_to_move)
      stack[from_stack] = stack[from_stack][:idx_to_slice_from]

part_1 = "".join([stack[len(stack) - 1].replace("[", "").replace("]", "") for stack in stacks_p1])
part_2 = "".join([stack[len(stack) - 1].replace("[", "").replace("]", "") for stack in stacks_p2])

print(f"Part 1: {part_1}")
print(f"Part 2: {part_2}")
