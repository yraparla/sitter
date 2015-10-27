import json
import re

judges = {}

# Count the number of sittings per judge for any given month
def count_sittings(month=""):
	with open('sittings.json', 'r') as f:
		panels = json.load(f)
		for panel in panels:
			if re.search(month, panel["panel"]):
				j = panel["judges"]
				if len(j) > 1:
					for judge in j:
						if judge not in judges:
							judges[judge] = 1
						else:
							judges[judge] = judges[judge] + 1
	return judges
print(count_sittings())