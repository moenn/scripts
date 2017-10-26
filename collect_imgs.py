'''
10/1/17
将 downloads 中的所有图片转移到当前目录中的 img 文件夹中去。  
(windows 系统下.)
'''

import os

img_extension = ('.jpeg', '.jpg', '.gif', '.png')
coldir = "C:\\Users\\jms29\\Downloads"
imgdir = os.path.join(coldir, 'img')


if not os.path.exists(imgdir):
	os.mkdir(imgdir)


for n in os.listdir(coldir):
	if n.endswith(img_extension):
		os.rename(os.path.join(coldir, n), os.path.join(imgdir, n))


