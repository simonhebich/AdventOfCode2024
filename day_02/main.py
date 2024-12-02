reports = []

# read file and save in two arrays
with open("input", "r") as input:
  reports = input.read().splitlines()

def check(report, damp):
  levels = [int(level) for level in report.split(" ")]
  
  
  # calculate differences
  diffs = [level - nextLevel for level, nextLevel in zip(levels[:-1], levels[1:])]
  
  # check conditions
  if not damp:
    incOrDec = all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
    spacing = not any((abs(diff) < 1 or abs(diff) > 3) for diff in diffs)
  else:
    incOrDec = sum(diff > 0 for diff in diffs) <= 1 or sum(diff < 0 for diff in diffs) <= 1
    spacing = sum((abs(diff) < 1 or abs(diff) > 3) for diff in diffs) <= 1

  return incOrDec and spacing



print(sum([check(report, False) for report in reports]))
print(sum([check(report, True) for report in reports]))
