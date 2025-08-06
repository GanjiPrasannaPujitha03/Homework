import os
import glob

# Step 1: Set paths
current_directory = os.getcwd()
input_folder = os.path.join(current_directory, "data_input")
output_folder = os.path.join(current_directory, "data_output")

# Step 2: Create folders if needed
if not os.path.exists(input_folder):
    os.mkdir(input_folder)
    print("🔔 'data_input' folder created. Please add .txt files and run again.")
    exit()

if not os.path.exists(output_folder):
    os.mkdir(output_folder)

# Step 3: Find .txt files
txt_files = glob.glob(os.path.join(input_folder, "*.txt"))
if not txt_files:
    print("⚠️ No .txt files found in data_input. Please add files and run again.")
    exit()

# Step 4: Process each file and store summary data
summary_data = []

for file_path in txt_files:
    filename = os.path.basename(file_path)
    line_count = 0
    word_count = 0
    modified_lines = []

    with open(file_path, "r") as f:
        for line in f:
            if line.strip().startswith("#"):
                continue
            line_count += 1
            word_count += len(line.split())
            new_line = line.replace("temp", "permanent")
            modified_lines.append(new_line)

    # Save modified file
    output_path = os.path.join(output_folder, filename)
    with open(output_path, "w") as f:
        f.writelines(modified_lines)

    summary_data.append((filename, line_count, word_count))
    print(f"✅ {filename} processed: {line_count} lines, {word_count} words")

# Step 5: Write summary.txt
summary_path = os.path.join(output_folder, "summary.txt")
with open(summary_path, "w") as summary_file:
    for filename, lines, words in summary_data:
        summary_file.write(f"Filename: {filename}\n")
        summary_file.write(f"Lines (excluding comments): {lines}\n")
        summary_file.write(f"Words (excluding comments): {words}\n")
        summary_file.write("\n")

print("\n📄 summary.txt created in data_output folder.")
