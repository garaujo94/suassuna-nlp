#!/bin/bash

echo "Starting virtual environment..."
source env/bin/activate
echo "Starting virtual environment...OK"

echo "Starting App..."
streamlit run main.py