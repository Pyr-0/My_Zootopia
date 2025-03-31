import json

def load_data(file_path):
	"""" Loads JSON file """
	with open(file_path, 'r') as handle:
		return json.load(handle)
	

def read_template(file_path):
	"""Reads the HTML template file"""
	with open(file_path, "r") as handle:
		return handle.read()

def write_html(file_path, content):
	"""Writes the generated HTML to a file"""
	with open(file_path, "w") as handle:
		handle.write(content)


""""Load JSON data"""
animals_data = load_data("animals_data.json")


for animal in animals_data:
	# Print the name (all animals should have a name)
	print(f"Name: {animal['name']}")
		
	# Print diet information (from the characteristics dictionary)
	if 'characteristics' in animal and 'diet' in animal['characteristics']:
		print(f"Diet: {animal['characteristics']['diet']}")
		
	# Print the first location (if locations exist and have items)
	if 'locations' in animal and len(animal['locations']) > 0:
		print(f"Location: {animal['locations'][0]}")
		
	# Print the type (if it exists)
	if 'type' in animal:
		print(f"Type: {animal['type']}")
		
	# Print an empty line after each animal for better readability
	print()