# Advent of Code
# Day 3 - Part 2 
# Finds the common compartment in each rucksack.
#
# Author: Kurt Campbell
# Date: 13 December 2022

ELVES_PER_GROUP = 3

input = open("input.txt")

common_badges = []
elf_group = []

# Emptys the elf group
def empty_elf_group():
    for i in range(ELVES_PER_GROUP):
        elf_group.pop()

# Gathers three rucksacks at time to represent the
# three elves. The goal of this implementation is to find
# the common badge between each elf.
line = input.readline()
while line != "":
    elf_group.append(line.strip())

    for i in range(ELVES_PER_GROUP - 1):
        line = input.readline()
        elf_group.append(line.strip())

    # Declares each rucksack into their own variables. 
    first_rucksack = elf_group[0]
    second_rucksack = elf_group[1]
    third_rucksack = elf_group[2]

    # Finds the common badge within these three rucksacks.
    for j in range (len(first_rucksack)):
        if second_rucksack.find(first_rucksack[j]) != -1:
            if third_rucksack.find(first_rucksack[j]) != -1:
                letter_unicode = ord(first_rucksack[j])
                if letter_unicode > 96:
                    common_badges.append(letter_unicode - 96)
                else:
                    common_badges.append(letter_unicode - 38)

                empty_elf_group()
                break

    line = input.readline()

sum = 0
for i in range(len(common_badges)):
    sum += common_badges.pop(0)
    
print("Sum: " + str(sum))