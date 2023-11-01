import subprocess
import time

# Replace with your GitHub username and repository name
github_username = "sivabalanb"
repository_name = " PythonSnippets"

# Number of commits you want to make
num_commits = 2

# Content for the commits
commit_message = "Automated commit test."

for i in range(num_commits):
    # Create or modify a file with a timestamp
    timestamp = time.time()
    filename = f"commit_{i}.txt"
    with open(filename, "w") as file:
        file.write(f"Commit {i} at {timestamp}")

    # Stage and commit the changes
    subprocess.run(["git", "add", filename])
    subprocess.run(["git", "commit", "-m", commit_message])

    # Push the changes to the repository
    subprocess.run(["git", "push", "origin", "main"])  # Replace 'main' with your branch name

print(f"{num_commits} commits made to the repository.")
