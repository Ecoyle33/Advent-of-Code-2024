#Create two lists, each list contains one column from input.txt
list1 = []
list2 = []

with open('Q1\input.txt', 'r') as f:
    
    for line in f:
        entry1, entry2 = line.strip().split()
        list1.append(entry1)
        list2.append(entry2)

list1 = [int(x) for x in list1]
list2 = [int(x) for x in list2]

list1.sort()
list2.sort()

totalDist = 0

# Equal length, can choose either list for range
for i in range(len(list1)):
    
    element1 = list1[i]
    element2 = list2[i]

    dist = abs(element2 - element1)

    totalDist += dist

print(totalDist)

# --Part 2--
similarityScore = 0

# For each element in list1
for i in range(len(list1)):
    
    element1 = list1[i]
    n = 0 #number of appearances

    for j in range(len(list2)):
        element2 = list2[j]
        if (element1 == element2):
            n += 1

    similarityScore += (element1 * n)

print(similarityScore)