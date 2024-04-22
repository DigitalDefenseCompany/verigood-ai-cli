import os

# List of files to combine
files = [
    "README.md",
    "_posts/2023-12-21-unified-diffs.md",
    "aider/__init__.py",
    "aider/coders/base_coder.py",
    "aider/coders/base_prompts.py",
    "aider/coders/udiff_coder.py",
    "aider/coders/udiff_prompts.py",
    "aider/commands.py",
    "aider/diffs.py",
    "aider/dump.py",
    "aider/history.py",
    "aider/io.py",
    "aider/main.py",
    "aider/mdstream.py",
    "aider/models.py",
    "aider/prompts.py",
    "aider/repo.py",
    "aider/repomap.py",
    "aider/scrape.py",
    "aider/sendchat.py",
    "aider/utils.py",
    "aider/versioncheck.py",
    "aider/voice.py",
    "docs/commands.md",
    "docs/faq.md",
    "docs/unified-diffs.md",
    "setup.py"
]

# Determine the directory of the current script file
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the output directory and ensure it exists
output_dir = os.path.join(script_dir, "out")
os.makedirs(output_dir, exist_ok=True)

# Define the path for the combined output file
output_file = os.path.join(output_dir, "combined_files.txt")

# Delimiter for separating file contents
delimiter = "\n" + "-"*80 + "\n"  # 80 dashes as a delimiter

with open(output_file, 'w') as outfile:
    for file_path in files:
        if os.path.exists(file_path):  # Check if the file exists
            outfile.write(f"File: {file_path}\n\n")  # Heading for each file
            with open(file_path, 'r') as file:
                outfile.write(file.read())  # Write the content of the file
            outfile.write(delimiter)  # Add delimiter after each file
        else:
            print(f"Warning: '{file_path}' does not exist and will be skipped.")

print(f"All files have been combined into {output_file}.")
