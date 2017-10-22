import sys, datetime

TEMPLATE = """


:modified: {timestamp}
:tags:
:summary:

"""

def make_entry(fn):
	template = TEMPLATE.format(timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))

	with open(fn, 'a') as f:
		f.write(template)

	print("File created -> " + fn)


if __name__ == '__main__':

	if len(sys.argv[1]) > 1:
		make_entry(sys.argv[1])

	else:
		print("No filename given")
