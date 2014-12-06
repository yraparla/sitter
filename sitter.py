#!/usr/bin/env python

# ---
# sitter.py
# A scraper and parser for the US Court of Appeals for the Federal Circuit
# License: MIT
#

# import modules
import re
from lxml import html
import json

f = html.parse('upcoming-oral-arguments.html')	# Parse the file
elements = f.findall("//tr/td")					# Get the cells from the table

# Initialize iterators
panel = []
i = 0

# ToDo: Add ignore case
pattern = "([A-Z]+:\s)([\w\']+)(,\s)([\w\']+)(,?\s\&?\s?)([\w\']+)"

# Loop the the cells in the table
for cell in elements:
	t = cell.text_content()

	# Check to see if this is a panel cell, and if it is, create a "panel" object
	if re.match("Panel",t):
		panel.append({"panel":t, "judges":[], "cases": []})
	else:

		# If it's not a panel cell, check to see if it's a judge cell, and if it is add to the "judges" array
		if len(panel) >= 1 and re.match(pattern, t, flags=re.IGNORECASE):	# Make sure it's not front matter 
			j = re.match(pattern, t,flags=re.IGNORECASE)
			panel[len(panel) - 1]["judges"] = [j.group(2), j.group(4), j.group(6)]	

		# If it's not a panel or judges cell, check to see if it's a case number cell, and if it is add to the "cases" array
		elif len(panel) >= 1 and re.match("\d+-\d+",t):
			panel[len(panel) - 1]["cases"].append(t) 

# Dump the object to file
print json.dumps(panel, indent=2)
