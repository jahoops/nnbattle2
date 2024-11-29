#!/bin/bash

# Navigate to the nnbattle2 directoryt

# Create directory structure
mkdir -p connect4-ai/data/raw
mkdir -p connect4-ai/data/processed
mkdir -p connect4-ai/data/external
mkdir -p connect4-ai/models/saved_models
mkdir -p connect4-ai/models/checkpoints
mkdir -p connect4-ai/notebooks
mkdir -p connect4-ai/src
mkdir -p connect4-ai/tests
mkdir -p connect4-ai/scripts

# Create empty Python files
touch connect4-ai/src/__init__.py
touch connect4-ai/src/data_preprocessing.py
touch connect4-ai/src/model.py
touch connect4-ai/src/train.py
touch connect4-ai/src/evaluate.py

touch connect4-ai/tests/__init__.py
touch connect4-ai/tests/test_data_preprocessing.py
touch connect4-ai/tests/test_model.py
touch connect4-ai/tests/test_train.py

# Create script files
touch connect4-ai/scripts/run_training.sh
touch connect4-ai/scripts/run_evaluation.sh

# Create other necessary files
touch connect4-ai/requirements.txt
touch connect4-ai/README.md
touch connect4-ai/setup.py

echo "Directory structure created successfully."