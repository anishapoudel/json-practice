import json

input_file = 'data/schacon.repos.json'
output_file = 'chacon.csv'

# Open the JSON file and load its content
with open(input_file, 'r') as file:
    data = json.load(file)

# Open the CSV file for writing
with open(output_file, 'w') as file:
    # Process only the first 5 repository entries
    for repo in data[:5]:
        name = repo['name']
        html_url = repo['html_url']
        updated_at = repo['updated_at']
        visibility = repo['visibility']
        file.write(f"{name},{html_url},{updated_at},{visibility}\n")