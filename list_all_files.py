'''
10/1/17
打印出 windows 电脑中的所有文件. (只装了 C 盘的情况下)
'''

import os

origin = 'C:\\'

def list_all_files(file):
	try:
		for n in os.listdir(file):
			filename = os.path.join(file, n)
			if os.path.isdir(filename):
				list_all_files(filename)
			else:
				print(filename)

	except:
		print("can't open",file)


if __name__ == '__main__':
	list_all_files(origin)
	

