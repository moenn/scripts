import sys
from subprocess import call

url_text = "C:\Users\jms29\Downloads\you-get-download\**.txt"
_dir = r"C:\Users\jms29\Downloads\you-get-download"

with open(url_text,"r") as f:
	url_lists = f.readlines()
	
for url in url_lists:
	call("you-get" + " -d " + url + " -o " + _dir + " -x 127.0.0.1:1080 ")