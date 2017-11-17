#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


boyname = [
	'漓','殇','梦','阑','雪','凪','爱','羽','魑','蔷','海','雨','悠','紫',
	'岚','晗','薰','柊','茵','钰','雅','夏','绪','栩','珣','菀',
	'琬','梧','霆','诗','丝','洛','温','蒂','璃','安','洁','莉','灵','血','魅','塔',
	'利','亚','伤','瑟','薇','玫','瑰','泪','邪','儿','凡','多','姆','威','恩','影','琉',
	'冰','伊','如','落','心','语','凌','陌','千','优','晶','墨','阳','云',
	'筱','残','莲','沫','渺','琴','依','然','可','黎','幽','幻','银','倾','乐','慕',
	'文','思','清','碎','音','芊','怡','苏','城','萌','美','迷','离','白','嫩','风','霜',
	'萝','妖','百','合','珠','喃','之','情','弥','绯','芸','茜','魂','澪','琪','欣',
	'咝','蠫','赬','飖','呗','缈','娅','吉','拉','斯','基','柔','朵','铃','裳',
	'纱','塲','颖','觞','蕴','燢','覮','铧','累','觷','儠','摋','孆','瞲','櫗','刿',
	'鷡','氩','浅','趯','鸑','萦','儽','骅','糜','婺','嚻','龠','鹦','韎','麴','莳','寂','翼',
	'巧','哀','俏','涅','盘','辰','芝','艾','柒','曼','妲','眉','御','寇','米',
	'菲','奥','格','萨','尼','子','克','乃','湿',
]

girlname = [
	'蝶','樱','莹','萤','滢','莺','璎','韵','舞','莎','姗','黛','丽','娜','瑷',
	'妮','娥','惠','茹','香','艳','花','茉','蕊','娥','妲','馨','倩','恋','妙',
]


def generate_pieces(sequence,num):
	pieces_list = []
	while num > 0:
		pieces_list.append(random.choice(sequence))
		num = num - 1 
	pieces = ''.join(pieces_list)
	return pieces



def create_name(sequence,length,firstname,lastname):
	name_list = []
	if firstname != '':
		name_list.append(firstname)

	count_len = 0
	while count_len < length:
		i = random.randint(1,5)
		pieces = generate_pieces(sequence,i)
		name_list.append(pieces)

		count_len += i
	if lastname != '':
		name_list.append(lastname)
	name = '·'.join(name_list)

	return name


if __name__ == '__main__':
	print('是否将你的姓与名显示在生成的名字中？要显示则在下面的选项中键入相应字段并回车，否则直接回车。')
	firstname = input('名：')
	lastname = input('姓:')
	name = create_name(boyname,10,firstname,lastname)
	print(name)