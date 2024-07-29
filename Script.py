import re
import argparse
import os

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

# Create the new file name with 'Corregido' appended
base_name, ext = os.path.splitext(file_path)
new_file_path = f"{base_name}_Corregida{ext}"

# Write the modified content to the new file
with open(new_file_path, 'w') as new_file:
    new_file.write(new_content)

print(f"Reemplazo completado. Archivo guardado como {new_file_path}.")
