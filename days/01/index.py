file_contents = open("days/01/input.txt", "r").read()
elves = file_contents.split("\n\n")
total_elf_calories = []
for elf in elves:
  elf_calories = [calorie for calorie in elf.split("\n") if calorie != ""]
  total = 0
  for calorie_count in elf_calories:
    total += int(calorie_count)
  total_elf_calories.append(total)

total_elf_calories.sort(reverse=True)
print("Part 1: " + str(total_elf_calories[0]))
print("Part 2: " + str(total_elf_calories[0] + total_elf_calories[1] + total_elf_calories[2]))