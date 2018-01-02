'''
生成一个玛丽苏名字
男性名字示例：氩·漓·凌洁晗·蕴霜龠基萨·文·情晗珣·糜黎萨弥优·巧文米盘儠
女性名字示例：莹姗·萤琪姗丽菲·艳丽丽妲·蕊依舞筱·瑷钰美·花恋娜

11/21/2017
'''
import random


boyname = [
	'漓','殇','梦','阑','雪','凪','爱','羽','魑','蔷','海','雨','悠','紫',
	'岚','晗','柊','雅','夏','绪','栩','珣','菀',
	'琬','梧','霆','诗','丝','洛','温','安','洁','灵','血','魅','塔',
	'利','亚','伤','泪','邪','儿','凡','多','姆','威','恩','影','琉',
	'冰','伊','如','落','心','语','凌','陌','千','优','晶','墨','阳','云',
	'残','渺','然','可','黎','幽','幻','银','倾','乐','慕',
	'文','清','碎','城','迷','离','白','嫩','风','霜',
	'妖','百','合','珠','喃','之','情','弥','绯','魂','澪',
	'咝','蠫','赬','飖','呗','缈','娅','吉','拉','斯','基','柔',
	'纱','塲','颖','觞','蕴','燢','覮','铧','累','觷','儠','摋','孆','瞲','櫗','刿',
	'鷡','氩','浅','趯','鸑','萦','儽','骅','糜','婺','嚻','龠','鹦','韎','麴','莳','寂','翼',
	'巧','哀','俏','涅','盘','辰','芝','艾','柒','曼','妲','眉','御','寇','米',
	'奥','格','萨','尼','子','克','乃','湿',
]

girlname = [
	'蝶','樱','莹','萤','滢','莺','璎','韵','舞','莎','姗','黛','丽','娜','瑷',
	'妮','娥','惠','茹','香','艳','花','茉','蕊','娥','妲','馨','倩','恋','妙',
	'薰','茵','钰','蒂','璃','莉','瑟','薇','玫','瑰','筱','莲','沫','芊','怡',
	'思','音','苏','琴','依','萌','美','萝','芸','茜','琪','欣','朵','铃','裳',
	'菲',

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
	try:
		gender = input('生成男生名字还是女生名字？(键入"F"为女生，键入"M"为男生): ').lower()
		length = int(input('请键入生成长度(5-50):  '))
		assert 5 <= length <= 50
		print('是否将你的姓与名显示在生成的名字中？要显示则在下面的选项中键入相应字段并回车，否则直接回车。')
		firstname = input('名： ')
		lastname = input('姓: ')
		if(gender == 'f'):
			name = create_name(girlname,length,firstname,lastname)
		elif(gender == 'm'):
			name = create_name(boyname,length,firstname,lastname)
		
		print(name)
	except:
		print('输入有误，退出程序')
		exit()