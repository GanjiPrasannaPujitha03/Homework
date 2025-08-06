import os
import shutil

# Q5: Move .txt files to "reports" folder

# Create 'reports' folder if it doesn't exist
reports_folder = "reports"
if not os.path.exists(reports_folder):
    os.mkdir(reports_folder)
    print("Created folder: reports")
else:
    print("reports folder already exists.")

# List all files in current directory
for file in os.listdir():
    if file.endswith(".txt"):
        print(f"Found text file: {file}")
        shutil.move(file, reports_folder)
        print(f"Moved {file} to reports/")
