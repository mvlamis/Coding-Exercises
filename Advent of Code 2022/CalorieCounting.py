# get text file input
txtfile = open("CalorieCountingInput.txt", "r")

bestElf = 0
elves = []
text = []
lines = txtfile.readlines()

for line in lines:
    if line != "\n":
        line = line.replace("\n", "")
        text.append(line)
    else:
        text.append("")

# count sum of lines and add to list
sum = 0
for line in text:
    if line != "":
        sum += int(line)
    else:
        if sum > bestElf:
            bestElf = sum
        sum = 0
    elves.append(sum)

# sort list
elves.sort()
elves.reverse()


topThree = 0
for i in range(3):
    topThree += elves[i]

print(topThree)
