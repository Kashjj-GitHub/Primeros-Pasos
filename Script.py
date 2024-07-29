import re
import argparse

# Set up argument parsing
parser = argparse.ArgumentParser(description='Replace a pattern in a text file using a regular expression.')
parser.add_argument('file_path', help='Path to the input text file')
args = parser.parse_args()

# Extract the file path from the arguments
file_path = args.file_path

# Define the regular expression pattern and the replacement text
pattern = r'(NG45Y)\s([0-9]{2,3}\sat\s[0-9]{4})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})\.([0-9]{2})\n'
replacement = r'\1\2-\3-\4 \5:\6:\7,'

# Read the content of the file
with open(file_path, 'r') as file:
    content = file.read()

# Replace the pattern using re.sub()
new_content = re.sub(pattern, replacement, content)

# Write the modified content back to the file
with open(file_path, 'w') as file:
    file.write(new_content)

print("Reemplazo completado.")
