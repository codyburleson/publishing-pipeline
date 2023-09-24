"""
This script performs the following tasks:
1. Traverses a given parent directory to find all Markdown files (with a .md extension)
   including those in its subdirectories.
2. Lists all the discovered Markdown files.
3. Uses Pandoc to compile and combine all these Markdown files into a single Markdown file named "combined.md".

Note: Ensure that Pandoc is installed and available in the system's PATH for this script to function correctly.
"""

import os
import subprocess
from datetime import datetime

# Constants
PARENT_FOLDER = "/mnt/c/Users/f77541a/repos/vietnam-war-story/Manuscript - Draft One"
# PARENT_FOLDER = "/mnt/c/Users/f77541a/repos/knowledge-base/2 Areas/Journal"
CURRENT_DATE = datetime.now().strftime('%Y-%m-%d_%H%M')
OUTPUT_FILE = f"/mnt/c/Users/f77541a/repos/vietnam-war-story/Compiled Manuscripts/{CURRENT_DATE} Manuscript.md"
NUM_FILES_TO_INCLUDE = -1  # Set to desired number or -1 for all files

def find_markdown_files(parent_folder):
    markdown_files = []

    for root, dirs, files in os.walk(parent_folder):
        for file in files:
            if file.endswith('.md'):
                full_path = os.path.join(root, file)
                markdown_files.append(full_path)

                # If we've reached the desired number of files and it's not set to -1, then stop collecting
                if 0 < NUM_FILES_TO_INCLUDE == len(markdown_files):
                    return markdown_files

    return markdown_files

def compile_with_pandoc(file_list, output_file):
    cmd = ["pandoc"] + ["--from","gfm"] + file_list + ["--filter","filter_remove_all_horz_rules.py"] + ["--wrap","preserve"] + ["--to","gfm"] + ["-o", output_file]
    print("Running command:", ' '.join(cmd))
    subprocess.run(cmd)

if __name__ == "__main__":
    markdown_files = find_markdown_files(PARENT_FOLDER)
    compile_with_pandoc(markdown_files, OUTPUT_FILE)
