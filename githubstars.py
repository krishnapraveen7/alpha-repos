import os
import base64
from github import Github
from dotenv import load_dotenv

load_dotenv()

# Replace with your personal access token and username
access_token = os.getenv("GITHUB_ACCESS_TOKEN")
# username = "krishnapraveen7"
# username = "karpathy"
username = "chiphuyen"
# username = "jph00"  # Jeremy howard
# username = "lucidrains"

# Initialize Github instance
g = Github(access_token)

# Get the user
user = g.get_user(username)

# Create a base directory to save the README files
base_dir = f"{username}_starred_repos"
os.makedirs(base_dir, exist_ok=True)

# Function to safely get content from a file
def safe_get_contents(repo, path):
    try:
        return repo.get_contents(path)
    except:
        return None

# Fetch README files from all starred repositories
for repo in user.get_starred():
    print(f"Fetching README from {repo.full_name}")
    
    # Create folder structure: owner/repo
    repo_dir = os.path.join(base_dir, repo.owner.login, repo.name)
    os.makedirs(repo_dir, exist_ok=True)


    
    # Try to get the README file
    readme_content = None
    for readme_name in ["README.md", "README", "readme.md", "readme", "README.rst", "readme.rst"]:
        readme_content = safe_get_contents(repo, readme_name)
        if readme_content:
            break
    

    try:
        if readme_content:
            # Decode content if it's base64 encoded
            if isinstance(readme_content.content, bytes) or isinstance(readme_content.content, str):
                content = base64.b64decode(readme_content.content).decode('utf-8')
            else:
                content = readme_content.content
            
            # Repo html url
            repo_html_url = repo.html_url
            header = f"# [{repo.name}]({repo_html_url})\n\n"
            content = header + content

            # Save the README content to a file
            actual_filename = f"{repo.owner.login}__{repo.name}__README.md"
            filename = os.path.join(repo_dir, actual_filename)

            with open(filename, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Saved README for {repo.full_name}")
        else:
            print(f"No README found for {repo.full_name}")
    except Exception as e:
        print(f"Error fetching README for {repo.full_name}: {e}")

print("Finished fetching README files from starred repositories.")