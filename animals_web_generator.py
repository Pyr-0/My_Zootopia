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


def serialize_animal(animal):
	"""Converts a single animal dictionary to HTML"""

	# Start with the opening list item tag
	output = '<li class="cards__item">\n'

	# Add the title (animal name)
	output += f'  <div class="card__title">{animal["name"]}</div>\n'

	# Start the card text div
	output += '  <div class="card__text">\n'

	# Start a proper list for animal details
	output += '	<ul class="animal-details">\n'

	# Add diet information
	if 'characteristics' in animal and 'diet' in animal['characteristics']:
		output += f'	  <li class="detail-item"><strong>Diet:</strong> {animal["characteristics"]["diet"]}</li>\n'

	# Add the first location
	if 'locations' in animal and len(animal['locations']) > 0:
		output += f'	  <li class="detail-item"><strong>Location:</strong> {animal["locations"][0]}</li>\n'

	# Add the type
	if 'type' in animal:
		output += f'	  <li class="detail-item"><strong>Type:</strong> {animal["type"]}</li>\n'
	
	# Close the lists and divs
	output += '	</ul>\n'
	output += '  </div>\n'
	output += '</li>\n'

	return output
def generate_animal_html():
	"""Main function to generate the animals HTML page"""
	# Load the animal data
	animals_data = load_data('animals_data.json')

	# Generate HTML for all animals
	animals_html = ''
	for animal in animals_data:
		animals_html += serialize_animal(animal)

	# Read the HTML template
	template = read_template('animals_template.html')
		
	# Replace the placeholder with our animal information
	final_html = template.replace('__REPLACE_ANIMALS_INFO__', animals_html)
		
	# Write the final HTML to a new file
	write_html('animals.html', final_html)
		
	print("HTML file generated successfully!")

# Run the main function
if __name__ == "__main__":
	generate_animal_html()
