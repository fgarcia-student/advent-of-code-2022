file_contents = open("days/04/input.txt").read()
pairs = [pair.split(",") for pair in file_contents.split("\n") if pair != ""]

full_overlap_count = 0
partial_overlap_count = 0
for pair in pairs:
  candidate_min_max_nums = [int(num) for num in "-".join(pair).split("-")]
  min_num = 9999999
  max_num = 0

  for num in candidate_min_max_nums:
    if (num <= min_num):
      min_num = num
    
    if (num >= max_num):
      max_num = num

  full_range = str(min_num) + "-" + str(max_num)
  if (full_range in pair):
    full_overlap_count += 1
  else:
    x1,x2,y1,y2 = candidate_min_max_nums
    if (x1 >= y1 and x1 <= y2 or y1 >= x1 and y1 <= x2):
      partial_overlap_count += 1

print("Part 1: " + str(full_overlap_count))
print("Part 2: " + str(full_overlap_count + partial_overlap_count))

