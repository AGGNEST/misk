
import pandas as pd
import json

# Read Excel file
df = pd.read_excel("kids-sentences.xlsx")

vocabulary = {}

for _, row in df.iterrows():

    word = str(row["Word"]).strip()

    # Skip empty words
    if pd.isna(row["Word"]):
        continue

    vocabulary[word.lower()] = {
        "word": word,
        "levels": {
            "1": [row["Sentence 1"]],
            "2": [row["Sentence 2"]],
            "3": [row["Sentence 3"]]
        }
    }

# Save JSON
with open("kids-sentences.json", "w", encoding="utf-8") as file:
    json.dump(vocabulary, file, ensure_ascii=False, indent=2)

print("Conversion completed successfully!")
print("Total words:", len(vocabulary))
