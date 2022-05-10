#! /bin/bash

if [ ! -d "venv" ]; then
    echo "Creating venv"
    python3 -m venv venv
fi

source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f "app/app.db" ];then
    echo "Creating database"
    source scripts/reset_db.cmd
fi
