# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "pandas",  # For working with tabular data
#   "httpx",   # Example HTTP client, can be removed if not needed
# ]
# ///

import csv
import sys

# Ensure the script takes the filename as a command-line argument
if len(sys.argv) != 2:
    print("Usage: uv run autolysis.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

try:
    with open(filename, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            print(row)
except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
    sys.exit(1)
