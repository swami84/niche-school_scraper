#!/bin/bash

# Git Repository Setup Script
echo "Setting up Git repository..."

# Initialize git repository
git init

# Create .gitignore file
cat > .gitignore << EOF
# Environment variables
.env

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
*.egg-info/
.installed.cfg
*.egg

# Jupyter Notebook
.ipynb_checkpoints

# Virtual environments
venv/
env/
ENV/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Logs
*.log

# Chrome driver (if using selenium)
chromedriver*
EOF

# Add all files
git add .

# Initial commit
git commit -m "Initial commit: School search and Niche scraper project

- Added SchoolSearcher with multiple search methods (DuckDuckGo, SerpAPI, Selenium)
- Added Firecrawl integration for web scraping
- Added Gemini Pro integration for content summarization
- Included comprehensive Jupyter notebook with full workflow
- Added requirements.txt and environment setup"

echo "Git repository initialized and initial commit created!"
echo ""
echo "Next steps:"
echo "1. Create a repository on GitHub/GitLab"
echo "2. Copy the remote URL"
echo "3. Run: git remote add origin <your-repo-url>"
echo "4. Run: git push -u origin main"
echo ""
echo "Or run the push_to_github.sh script after setting REPO_URL"