#! /bin/bash

pip install --upgrade pip
pip install -r requirements.txt

if [ ! -f "app/app.db" ];then
    echo "Creating database"
    source scripts/reset_db.cmd
fi
