input = open("input.txt")

lines = input.readlines()

fat_elf = 0
sum = 0

for line in lines:
    if len(line) != 1:
        newline_index = line.find("\n")
        if newline_index != -1:
            sum += int(line[:newline_index])
    else:
        if sum > fat_elf:
            fat_elf = sum 
        sum = 0

print("Fatest Elf: " + str(fat_elf))

input.close()
