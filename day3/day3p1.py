# Advent of Code
# Day 3 - Part 1
# Finds the common compartment in each rucksack.
#
# Author: Kurt Campbell
# Date: 12 December 2022

input = open("input.txt")

lines = input.readlines()

common_compartments = []

for line in lines:
    rucksack = line.strip()
    rucksack_length = len(rucksack)
    
    # Splits the rucksack in half
    first_half = rucksack[:rucksack_length / 2]
    second_half = rucksack[rucksack_length / 2:]

    # Enables this if the common compartment has already been stored
    # since we do not want duplicates.
    rucksack_common_priorty = False
    
    # Finds the common compartment between the first and second halves. 
    for i in range(rucksack_length / 2):
        for j in range(rucksack_length / 2):
            if first_half[i] == second_half[j]:
                letter_unicode = ord(first_half[i])
                if letter_unicode > 96 and not rucksack_common_priorty:
                    common_compartments.append(letter_unicode - 96)
                elif not rucksack_common_priorty:
                    common_compartments.append(letter_unicode - 38)
                    
                rucksack_common_priorty = True

    
    rucksack_common_priorty = False

# Sums up all the common compartments within all rucksacks.
sum = 0
for i in range(len(common_compartments)):
    sum += common_compartments.pop(0)

print("Sum: " + str(sum))

input.close()