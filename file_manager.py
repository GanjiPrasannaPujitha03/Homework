import os

# Q2: Check if a Path is a File or Directory
print("Current Working Directory:", os.getcwd())
path = input("Enter a path: ")

if os.path.isdir(path):
    print("It is a directory.")
elif os.path.isfile(path):
    print("It is a file.")
else:
    print("Invalid path.")

# Q3: Create a Directory (if not exists)
folder_name = "test_folder"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Created folder: {folder_name}")
else:
    print(f"{folder_name} already exists.")

# Q4: Loop Through Files and Filter by Extension
print("Txt folders are listed below")
for file in os.listdir():
    if file.endswith(".txt"):
        print(file)
