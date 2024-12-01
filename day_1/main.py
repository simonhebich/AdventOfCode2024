## Task 1 ##

list1 = []
list2 = []

# read file and save in two arrays
with open("input.txt", "r") as input:
    lines = input.read().splitlines()
    for line in lines:
      elem1, elem2 = line.rsplit("  ")
      list1.append(int(elem1))
      list2.append(int(elem2))

# compare elements and save difference
diff = 0
list1.sort()
list2.sort()

merged_list = zip(list1, list2)
for item in merged_list:
  diff += abs(item[0] - item[1])

# Solution 1: print difference score 
print(diff)

## Task 2
def kindaBucketSort(l):
  bucket = {}
  for elem in l:
    if elem in bucket.keys():
      bucket[elem] += 1
    else:
      bucket[elem] = 1
  return bucket

bucket1 = kindaBucketSort(list1)
bucket2 = kindaBucketSort(list2)

similarityScore = 0
for key in bucket1.keys():
  similarityScore += key * bucket1[key] * bucket2.get(key, 0)
  
print("Similarity Score: " + str(similarityScore))