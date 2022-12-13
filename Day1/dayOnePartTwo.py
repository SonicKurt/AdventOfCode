input = open("input.txt")

lines = input.readlines()

top_elves = [0, 0, 0]
TOP_ELVES_COUNTER = 3

fat_elf = 0
sum = 0

for line in lines:
    if len(line) != 1:
        newline_index = line.find("\n")
        if newline_index != -1:
            sum += int(line[:newline_index])
    else:
        elf_one = top_elves.pop(0)
        elf_two = top_elves.pop(0)
        elf_three = top_elves.pop(0)

        if sum >= elf_one:
            top_elves.append(sum)
            top_elves.append(elf_one)
            top_elves.append(elf_two)                        
        elif sum >= elf_two:
            top_elves.append(elf_one)
            top_elves.append(sum)
            top_elves.append(elf_two)
        elif sum >= elf_three:
            top_elves.append(elf_one)
            top_elves.append(elf_two)
            top_elves.append(sum)
        else:
            top_elves.append(elf_one)
            top_elves.append(elf_two)
            top_elves.append(elf_three)

        sum = 0
            
total_elves_calories = 0
for i in range(TOP_ELVES_COUNTER):
    total_elves_calories += top_elves.pop(0)

print("Top Three Elves Total: " + str(total_elves_calories))

input.close()