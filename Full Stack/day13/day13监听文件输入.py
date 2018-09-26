def tail(filename):
	f = open(filename, encoding = 'utf-8')
	while True:
		line = f.readline()
		if line.strip():
			yield line.strip()

g = tail('file.txt')
for i in g:
	if 'python' in i:
		print(i)