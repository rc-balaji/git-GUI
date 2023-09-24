import os
import git

# Get user input for the root directory path
root_dir = input("Enter the root directory path: ")

# Get user input for the branch name
branch_name ="main"#input("Enter the branch name: ")

# Get user input for the Git repository URL
git_url = input("Enter the Git repository URL: ")

# Initialize a Git repository in the root directory
repo = git.Repo.init(root_dir)

try:
    # Add files to the staging area
    repo.git.add(A=True)

    # Commit the changes
    repo.git.commit('-m', 'Auto commit')

    # Rename the branch to the specified branch name
    repo.git.branch('-M', branch_name)

    # Add the remote repository with the provided URL
    repo.create_remote('custom_remote', git_url)

    # Push to the specified branch on the custom remote repository
    repo.git.push('custom_remote', branch_name)

    print(f"Pushed to the {branch_name} branch on your custom remote repository.")
except Exception as e:
    print("Error:", e)
