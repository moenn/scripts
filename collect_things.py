'''
10/1/17
把指定目录中某格式的所有文件移动到相应的文件夹中。
如：把 downloads 目录中所有图片移动到 image 文件夹中。
'''
import os


original_dir = "C:\\Users\\jms29\\Downloads"

videodir = os.path.join(original_dir, 'video')
imgdir = os.path.join(original_dir, 'img')
target_dirs = [videodir, imgdir]

video_ends = ('.torrent', '.mp4', '.avi', '.rmvb', '.mkv')
img_ends = ('.jpeg', '.jpg', '.gif', '.png')
ends = [video_ends, img_ends]

args = dict(zip(target_dirs, ends))


def makedirs(dirs):
	for n in dirs:
		if not os.path.exists(n):
			os.mkdir(n)

def move_files(_dir, args):
	for n in os.listdir(_dir):
		for directory,ends in args.items():

			if n.endswith(ends):
				os.rename(os.path.join(_dir, n), os.path.join(directory, n))


if __name__ == '__main__':
	
	makedirs(target_dirs)
	move_files(original_dir, args)
