import os

# Define project structure
project_structure = {
    "sec_threat_keyword_hunter": {
        "app": [
            "admin_dashboard.py",
            "clearweb_crawler.py",
            "darknet_crawler.py",
            "data_extractor.py",
            "user_dashboard.py",
            "models.py",
            "auth.py",
            "utils.py",
            "main.py",
            {
                "templates": [
                    "landing.html",
                    "admin_dashboard.html",
                    "user_dashboard.html",
                    "signup.html",
                    "login.html",
                    "log.html"
                ]
            }
        ],
        ".": ["requirements.txt", "README.md"]
    }
}

# Create the directories and files
def create_structure(base_path, structure):
    for key, value in structure.items():
        # Create main directory
        directory_path = os.path.join(base_path, key)
        os.makedirs(directory_path, exist_ok=True)

        for item in value:
            if isinstance(item, dict):
                # Recursive call for nested directories
                create_structure(directory_path, item)
            else:
                # Create files
                file_path = os.path.join(directory_path, item)
                with open(file_path, 'w') as f:
                    f.write("# Placeholder content\n")  # Add basic placeholder content

def write_requirements():
    requirements = """
Flask
SQLAlchemy
requests
beautifulsoup4
werkzeug
    """
    with open("sec_threat_keyword_hunter/requirements.txt", "w") as req_file:
        req_file.write(requirements.strip())

def write_readme():
    readme_content = """
# SEC Threat Keyword Hunter

This project provides a web application to crawl the web and dark web for specific keywords related to SEC threats.

## Project Structure
- `app/`: Contains the main application files including crawlers, models, and dashboards.
- `templates/`: HTML templates for the front-end.
- `requirements.txt`: Project dependencies.
- `README.md`: Project overview and instructions.
"""
    with open("sec_threat_keyword_hunter/README.md", "w") as readme_file:
        readme_file.write(readme_content)

# Deploy using Genezio (assumes Genezio CLI is installed and configured)
def deploy_genezio():
    os.system("cd sec_threat_keyword_hunter && genezio deploy")

# Create project structure
base_path = os.getcwd()
create_structure(base_path, project_structure)

# Write additional files
write_requirements()
write_readme()

# Deploy with Genezio
deploy_genezio()

print("Project structure created and deployed successfully.")
