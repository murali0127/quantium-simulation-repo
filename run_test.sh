#!/bin/bash

source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
pip install "dash[testing]"

# Run tests
pytest

if [ $? -eq 0 ]; then
    echo "All tests passed"
    exit 0
else
    echo "Tests failed"
    exit 1
fi