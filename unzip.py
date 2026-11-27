import zipfile
import os

zip_folder = r"C:\Users\aaabd\Downloads\images.cv"
extract_folder = r"C:\Users\aaabd\OneDrive\سطح المكتب\SIC_AI_Course\misk-samsung\misk-samsung\extracted"

os.makedirs(extract_folder, exist_ok=True)

for file in os.listdir(zip_folder):
    if file.endswith(".zip"):
        zip_path = os.path.join(zip_folder, file)

        with zipfile.ZipFile(zip_path, "r") as zip_ref:
            zip_ref.extractall(extract_folder)

        print(f"Extracted: {file}")

print("All files extracted successfully!")