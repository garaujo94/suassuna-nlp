#!/bin/bash

echo "Creating virtual environment..."
python3 -m venv env
echo "Creating virtual environment...OK"

echo "Starting virtual environment..."
source env/bin/activate
echo "Starting virtual environment...OK"

echo "Installing dependencies..."
pip install -r requirements.txt

pip install -U pip setuptools wheel
pip install -U spacy

python -m spacy download en_core_web_lg
python -m spacy download pt_core_news_lg
echo "Installing dependencies...OK"

deactivate

echo "Finished!"