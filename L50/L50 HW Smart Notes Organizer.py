# SMART NOTES ORGANIZER
# Topics: read(n) | readlines() | Loop Through File | Filter Lines | Write Selected Lines

# PART 1 -- Sneak Peek
n = int(input("How many characters to preview? "))

file = open("L50/smart-notes.txt", "r")
print(file.read(n))

file.close()
print()


# PART 2 -- All lines as a list
file = open("L50/smart-notes.txt", "r")
lines = file.readlines()

file.close()

print("Total lines:", len(lines))

for i in range(len(lines)):
    print(i + 1, "->", lines[i].strip())

print()


# PART 3 -- Filter Important and TODO Lines
file = open("L50/smart-notes.txt", "r")

for line in file:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        print("keep ->", line.strip())
    else:
        print("skip ->", line.strip())

file.close()
print()


# PART 4 -- Save Important and TODO Lines to New File
file = open("L50/smart-notes.txt", "r")
lines = file.readlines()
file.close()

out = open("L50/clean-smart-notes.txt", "w")

for line in lines:
    if line.startswith("IMPORTANT") or line.startswith("TODO"):
        out.write(line)

out.close()

print("Clean notes saved to clean-smart-notes.txt")