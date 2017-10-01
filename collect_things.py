'''
10/1/17
把指定目录中某格式的所有文件移动到相应的文件夹中。
如：把 downloads 目录中所有图片移动到 image 文件夹中。
'''
import os


coldir = "C:\\Users\\jms29\\Downloads"

videodir = os.path.join(coldir, 'video')
imgdir = os.path.join(coldir, 'img')
dirs = [videodir, imgdir]

video_extensions = ('.torrent', '.mp4', '.avi', '.rmvb', '.mkv')
img_extensions = ('.jpeg', '.jpg', '.gif', '.png')
extensions = [video_extensions, img_extensions]

files = dict(zip(dirs, extensions))

def makedirs(dirs):
	for n in dirs:
		if not os.path.exists(n):
			os.mkdir(n)

def move_files(coldir, files):
	for n in os.listdir(coldir):
		for dir_,extension in files.items():

			if os.path.splitext(n)[1] in extension:
				os.rename(os.path.join(coldir, n), os.path.join(dir_, n))


if __name__ == '__main__':
	
	makedirs(dirs)
	move_files(coldir, files)
