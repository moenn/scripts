import os


fic = []
for n in os.listdir('./'):
	if os.path.isfile(n):
		if n.endswith('.txt'):
			fic.append(n)
	elif os.path.isdir(n):
		pass
	else:
		print('???')


for n in fic:
	print(n)