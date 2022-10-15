#!/bin/bash

cd project-22-fal-12-hackathon-team-2

git fetch && git reset origin/main --hard

# Install python virtual environment
python -m venv python3-virtualenv

# Enter python virtual environment
source python3-virtualenv/bin/activate

#install python dependencies
pip install -r requirements.txt

systemctl restart myportfolio