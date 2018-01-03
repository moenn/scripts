'''
计算文件的 md5 和 sha1 校验值
'''
import hashlib
import sys

BUF_SIZE = 65536

md5 = hashlib.md5()
sha1 = hashlib.sha1()


with open(sys.argv[1],'rb') as f:
	for chunk in iter(lambda:f.read(BUF_SIZE),b''):
		md5.update(chunk)
		sha1.update(chunk)

print("MD5:{0}".format(md5.hexdigest()))
print("SHA1:{0}".format(sha1.hexdigest()))

