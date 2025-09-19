import kagglehub
import shutil
import os

# Download latest version
path = kagglehub.dataset_download("atharvaingle/crop-recommendation-dataset")

print("Path to dataset files:", path)

# Find the CSV file in the downloaded directory
for root, dirs, files in os.walk(path):
    for file in files:
        if file.endswith('.csv') and 'crop' in file.lower():
            src = os.path.join(root, file)
            dst = os.path.join("data", "Crop_recommendation.csv")
            shutil.copy2(src, dst)
            print(f"Copied {file} to data/Crop_recommendation.csv")
            break
