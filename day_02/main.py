reports = []

# read file and save in two arrays
with open("test", "r") as input:
  reports = input.read().splitlines()

def check(report):
  levels = [int(level) for level in report.split(" ")]
  
  
  # calculate differences
  diffs = [level - nextLevel for level, nextLevel in zip(levels[:-1], levels[1:])]
  
  # check conditions
  incOrDec = all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
  spacing = not any((abs(diff) < 1 or abs(diff) > 3) for diff in diffs)
  
  return incOrDec and spacing

print(sum([check(report) for report in reports]))

## Task 2 ##

def dampCheck(report):
  levels = [int(level) for level in report.split(" ")]
  
  # calculate differences
  diffs = [level - nextLevel for level, nextLevel in zip(levels[:-1], levels[1:])]


  # Problem: both conditions can be = 1 which might be problematic but not necessary

  # Solution 1: Check conditions during iteration and directly remove the first problematic level. By the second prob. level we can abort
  life = 1
  lastDiff = diffs[0]
  i = 0
  end = len(diffs)
  while i < end:
    if life < 0:
      return False
    
    change = (lastDiff * diffs[i]) < 0
    wrongSpacing = abs(diffs[i]) < 1 or abs(diffs[i]) > 3
    if change or wrongSpacing:
      diffs = diffs[:i] ++ diffs[i:]
      life -= 1
      end -= 1
      continue
    i += 1
    lastDiff = diffs[i]
  return True
    
  # deprecated -> Solution 2: save safe state for for both cond. for every diff - then merge both and check prob. count

print(sum([dampCheck(report) for report in reports]))