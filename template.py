import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')

# Minimal structure tailored for Astro Insight Generator
list_of_files = [
    "src/__init__.py",
    "app.py",                 # Main app logic (CLI or FastAPI)
    "src/zodiac_utils.py",        # Zodiac sign calculation
    "src/insight_generator.py",   # Hardcoded insights or templates
    "setup.py",              # Package setup
    "research/trials.ipynb",  # Jupyter notebook for trials
    "requirements.txt",
    "README.md",             # Project documentation
    ".env"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass  # Create empty file
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists.")
