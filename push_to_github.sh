#!/bin/bash

# Push to GitHub Script
# Usage: ./push_to_github.sh <repository-url>
# Example: ./push_to_github.sh https://github.com/username/repo-name.git

if [ $# -eq 0 ]; then
    echo "Usage: $0 <repository-url>"
    echo "Example: $0 https://github.com/username/school-scraper.git"
    exit 1
fi

REPO_URL=$1

echo "Pushing to repository: $REPO_URL"

# Add remote origin
git remote add origin $REPO_URL

# Push to main branch
git branch -M main
git push -u origin main

echo "Successfully pushed to $REPO_URL"
echo "Your repository is now live!"