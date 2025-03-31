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


# Generate a string with all animal information
output = ''
for animal in animals_data:
	# Add the name
	output += f"Name: {animal['name']}\n"
		
	# Add diet information
	if 'characteristics' in animal and 'diet' in animal['characteristics']:
		output += f"Diet: {animal['characteristics']['diet']}\n"
		
	# Add the first location
	if 'locations' in animal and len(animal['locations']) > 0:
		output += f"Location: {animal['locations'][0]}\n"
		
	# Add the type
	if 'type' in animal:
		output += f"Type: {animal['type']}\n"
		
	output += "\n"

template = read_template('animals_template.html')

final_html = template.replace('__REPLACE_ANIMALS_INFO__', output)

write_html('animals.html', final_html)