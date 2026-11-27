from pathlib import Path

words = []

with open("kids-words.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if not line or line.startswith("#"):
            continue

        word = line.split("|")[0].strip()
        words.append(word)

mid = (len(words) + 1) // 2

group1 = words[:mid]
group2 = words[mid:]

Path("group_1.txt").write_text(
    "\n".join(group1), encoding="utf-8"
)

Path("group_2.txt").write_text(
    "\n".join(group2), encoding="utf-8"
)

print("Total words:", len(words))
print("Group 1:", len(group1))
print("Group 2:", len(group2))