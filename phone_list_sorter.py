"""
This Python application take CPM phone list as text document and strips all but first and last names of each employee, stores
then in a list, alphabetizes according to last name, then creates new text document. Requires minimal manual formatting
of text file input.

Future dev goals:
Create save file of list as well as text output. Make script to fetch directly from intranet.
"""


# Define main function
def main():

	# Print introduction
	print("This Python application take CPM phone list as text document and strips all but first and last names.")
	print("It then creates a new text document with employees sorted my last name.")
	print("")

	# open 'raw_phone_list' text file
	raw_list = open("raw_phone_list.txt", "r")
	# designate file to read
	personnel = raw_list.read()
	# partition file at consistent undesireable elements and remove those sections
	personnel = personnel.partition("98109")
	personnel = personnel[2]
	personnel = personnel.partition("Internal")
	personnel = personnel[0]
	personnel.replace("Mobile", " ")

	# Remove 'Mobile' label from phone contacts
	while "Mobile" in personnel:
			personnel = personnel.partition("Mobile")
			personnel = (personnel[0] + personnel[2])

	# Replace 'dots' in phone # formatting with no character
	personnel = personnel.replace(".", "")

	# Replace digits in phone #s with no chars, effectively removing numbers from list
	for any_num in range (0, 10):
		any_num = str(any_num)
		personnel = personnel.replace(any_num, "")
	
	# Replace blank space and common extraneous contact labels with new line breaks
	personnel = personnel.replace("  ", "\n")
	personnel = personnel.replace("Reception", "\n")
	personnel = personnel.replace("reception", "\n")
	personnel = personnel.replace("Upstairs", "\n")
	personnel = personnel.replace("upstairs", "\n")

	# 'split' method breaks up long string and assigns to a list w/ same name
	personnel = personnel.split()

	# final garbage removal (stray unnatached characters)
	for e in personnel:
		if (len(e) < 2):
			personnel.remove(e)
		else:
			pass

	# Print 'personnel' list for testing
	print("personnel: ", personnel)

	# create iteration var based on number of elements in 'personnel' (first and last names) .. as integer
	full_count = int(len(personnel))
	fc = full_count

	# Creates iteration counter for looping (fc + 1)
	full_count_loop = int(fc + 1)
	fcl = full_count_loop

	# Creates iteration counter that is half the quantity of 'full count'. Not currently used
	half_count = int(len(personnel) / 2)
	hc = half_count

	# Create list for storing re-sorted elements (names)
	name_list = []

	# Loop through 'personnel' list and pop() items into x and y vars, swap values to put last name first, then store in 'name_list'.
	# Include exception handling... pass when out of range
	try:
		for item in range(0, fcl):
			x = personnel.pop(0)
			y = personnel.pop(0)
			x, y = y, x
			sorted_name = x + " " + y + "\n"
			name_list.append(sorted_name)
	except:
		pass

	name_list.sort()
	
	f = open("alphabetized_phone_list.txt", "w+")

	# Prints each item in newly populated 'name_list'
	for item in name_list:
		f.write(item)
	
	# Prints to screen for testing/ interface
	for item in name_list:
		print(item)
	
	# Close destination file
	f.close()

	# Close source file
	raw_list.close()

	# Just a blank line
	print("")
	input("Press 'enter' key to quit program.")
	quit()

# Call main function
main()







