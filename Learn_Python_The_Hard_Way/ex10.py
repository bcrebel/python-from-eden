"""while True: 
	for i in ["/","-","|", "\\","|"]: 
		print "%s\r" % i,

"""
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
#I'll do a list:
#\t* Cat food
#\t* Fishies
#\t* Catnip\n\t* Grass
"""

#print tabby_cat
catacademy = "%s %s" % (tabby_cat, persian_cat)
print catacademy 

dogacademy = "%r %r " % (tabby_cat, persian_cat)
print dogacademy
#print persian_cat
#print backslash_cat
#print fat_cat
