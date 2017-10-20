import sys, datetime

TEMP = """


:modified: {timestamp}
:tags:
:slug: {filename}
:summary:

"""

def make_entry(fn):
	fname = fn.split('/')[-1].split('.')[0]
	template = TEMP.format(timestamp=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), filename=fname)

	with open(fn, 'a') as f:
		f.write(template)

	print("File created -> " + fn)


if __name__ == '__main__':

	if len(sys.argv[1]) > 1:
		make_entry(sys.argv[1])

	else:
		print("No filename given")
