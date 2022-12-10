line = open("days/06/input.txt").read()

def decode(line, decode_limit):
  start_idx = 0
  end_idx = 0
  chars_seen = set(())
  for index in range(len(line)):
    char = line[index]
    if char in chars_seen:
      while char in chars_seen:
        chars_seen.remove(line[start_idx])
        start_idx += 1
    
    chars_seen.add(char)
    end_idx = index
    if (len(chars_seen) == decode_limit):
      return end_idx

print(f"Part 1: {decode(line, 4)}")
print(f"Part 2: {decode(line, 14)}")