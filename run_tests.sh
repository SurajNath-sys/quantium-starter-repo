#!/bin/bash

# Activate virtual environment
source venv/Scripts/activate

# Run the test suite
python -m pytest test_app.py -v

# Capture the exit code
EXIT_CODE=$?

# Return 0 if passed, 1 if failed
if [ $EXIT_CODE -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Tests failed!"
    exit 1
fi