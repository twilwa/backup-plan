#!/bin/bash

# Sync with the origin repository

git fetch origin main
status=$(git rev-parse --abbrev-ref HEAD)

if [[ "$status" != "main" ]]; then
    echo "Not on 'main' branch."
    exit 1
fi

# Check if local 'main' branch is behind the remote 'main' branch
behind=$(git rev-list --count HEAD..origin/main)

if [[ $behind -gt 0 ]]; then
    echo "Local 'main' branch is behind the remote. Updating..."
    git pull origin main
else
    echo "Local 'main' branch is up to date with remote."
fi
