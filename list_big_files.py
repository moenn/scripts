'''
10/1/17
打印出 windows 电脑中大于 1GB 的文件. (只装了 C 盘的情况下)
'''
import os

BIG_FILE_CRISIS = 1000000000  #  big file > 1GB   


origin = 'C:\\'
record = []

def get_big_files(file):
	try:
		for n in os.listdir(file):
			filename = os.path.join(file, n)
			if os.path.isdir(filename):
				get_big_files(filename)
			elif os.path.getsize(filename) > BIG_FILE_CRISIS: 
				record.append(filename)
			else:
				pass
	except:
		print("can't open", file)


if __name__ == '__main__':
	get_big_files(origin)

#打印大于 1GB 的文件
for n in record:
	print(n)