#!/bin/bash

# Make sure you are in the root directory of the repository

git fetch upstream
git merge upstream/main
git push origin main