'''
10/1/17
把指定目录中某格式的所有文件移动到相应的文件夹中。
如：把 downloads 目录中所有图片移动到 image 文件夹中。
'''
import os


original_dir = "C:\\Users\\jms29\\Downloads"

videodir = os.path.join(original_dir, 'video')
imgdir = os.path.join(original_dir, 'img')
tordir = os.path.join(original_dir, 'torrent')
target_dirs = [videodir, imgdir, tordir]

video_ends = ('.mp4', '.avi', '.rmvb', '.mkv', '.wmv')
img_ends = ('.jpeg', '.jpg', '.gif', '.png')
torrent_ends = ('.torrent')
ends = [video_ends, img_ends, torrent_ends]

args = dict(zip(target_dirs, ends))


def makedirs(dirs):
	for n in dirs:
		if not os.path.exists(n):
			os.mkdir(n)

def move_files(_dir, tings2move):
	for n in os.listdir(_dir):
		for dir2move,ends in tings2move.items():

			if n.endswith(ends):
				ori_dir = os.path.join(_dir, n)
				tar_dir = os.path.join(dir2move, n)
				os.rename(ori_dir, tar_dir)


if __name__ == '__main__':
	
	makedirs(target_dirs)
	move_files(original_dir, args)
