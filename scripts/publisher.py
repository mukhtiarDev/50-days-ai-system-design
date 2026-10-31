import os
import json
import glob
import re
import subprocess
from datetime import datetime, timezone

PROGRESS_FILE = "PROGRESS.json"

def run_cmd(command):
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode != 0:
        print(f"Error executing: {command}\n{result.stderr}")
    return result.stdout.strip()

def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, "r") as f:
            return json.load(f)
    return {"published_files": []}

def save_progress(data):
    with open(PROGRESS_FILE, "w") as f:
        json.dump(data, f, indent=2)

def extract_sort_key(filepath):
    """Extracts numbers from path/filename to sort lessons/problems correctly regardless of naming scheme."""
    numbers = re.findall(r'\d+', filepath.replace("\\", "/"))
    if numbers:
        # Convert the first found number sequence into an integer for proper sorting
        return int(numbers[0])
    return 999999

def main():
    print("Starting automated publishing check...")
    
    # Configure git user for automated commits
    run_cmd('git config --global user.name "GitHub Actions Bot"')
    run_cmd('git config --global user.email "actions@github.com"')

    progress = load_progress()
    published = set(progress["published_files"])

    # Find all potential content files (.md, .py, etc.) recursively across any subfolder structure
    all_files = glob.glob("**/*.md", recursive=True) + glob.glob("**/*.py", recursive=True)
    
    # Exclude system folders, scripts, tests, and root documentation files
    exclude_dirs = {".github", "scripts", "tests", "docs"}
    ignore_files = {"readme.md", "roadmap.md", "contributing.md", "manifest.json", "progress.md", "lesson_index.md"}
    
    valid_files = []
    for f in all_files:
        normalized_path = f.replace("\\", "/")
        parts = normalized_path.split("/")
        
        if any(d in exclude_dirs for d in parts):
            continue
        if os.path.basename(f).lower() in ignore_files:
            continue
            
        valid_files.append(normalized_path)

    # Sort files intelligently based on their numerical ordering
    valid_files.sort(key=extract_sort_key)

    # Find the next unpublished file
    next_file = None
    for file in valid_files:
        if file not in published:
            next_file = file
            break

    if not next_file:
        print("🎉 All content has already been published!")
        return

    print(f"Publishing today's file: {next_file}")

    # Stage the file
    run_cmd(f'git add "{next_file}"')
    
    # Update progress record
    published.add(next_file)
    progress["published_files"] = list(published)
    progress["last_published_date"] = datetime.now(timezone.utc).isoformat()
    save_progress(progress)
    
    run_cmd(f'git add {PROGRESS_FILE}')
    
    # Commit and push changes
    commit_msg = f"daily-publish: Automated release of {os.path.basename(next_file)}"
    run_cmd(f'git commit -m "{commit_msg}"')
    
    push_output = run_cmd('git push origin HEAD:main')
    print("Successfully pushed today's update!", push_output)

if __name__ == "__main__":
    main()