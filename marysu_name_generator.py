'''
生成一个玛丽苏名字
男性名字示例：氩·漓·凌洁晗·蕴霜龠基萨·文·情晗珣·糜黎萨弥优·巧文米盘儠
女性名字示例：莹姗·萤琪姗丽菲·艳丽丽妲·蕊依舞筱·瑷钰美·花恋娜

11/21/2017
'''
import random

malepieces = [

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

femalepieces = [
	'蝶','樱','莹','萤','滢','莺','璎','韵','舞','莎','姗','黛','丽','娜','瑷',
	'妮','娥','惠','茹','香','艳','花','茉','蕊','娥','妲','馨','倩','恋','妙',
	'薰','茵','钰','蒂','璃','莉','瑟','薇','玫','瑰','筱','莲','沫','芊','怡',
	'思','音','苏','琴','依','萌','美','萝','芸','茜','琪','欣','朵','铃','裳',
	'菲',

]

#  使用 sequence 中的 num 个元素，组成一个 string。
def generate_pieces(sequence,num):
	pieces_list = []
	while num > 0:
		pieces_list.append(random.choice(sequence))
		num = num - 1 
	pieces = ''.join(pieces_list)
	return pieces


# 从 sequence 中抽取元素组成一个不长于 length 的 string。
def create_name(sequence,length,firstname,lastname):
	name_pieces = []
	if firstname != '':
		name_pieces.append(firstname)

	count_len = 0
	while count_len < length:
		i = random.randint(1,5)
		name_pieces.append(generate_pieces(sequence,i))
		count_len += i
	
	if lastname != '':
		name_pieces.append(lastname)
	name = '·'.join(name_pieces)

	return name


if __name__ == '__main__':
	gender = input('生成男生名字还是女生名字？(键入"F"为女生，键入"M"为男生): ').lower()
	assert (gender == 'f' or gender == 'm')

	print('是否将你的姓与名添加到将生成的名字中？要添加则键入相应字段，否则直接回车。')
	firstname = input('名:	')
	lastname = input('姓:	')
	if(firstname == ''):
		print('不添加自己的名。')
	if(lastname == ''):
		print('不添加自己的姓。')
	raw = input('请键入生成长度(5-50)，随机长度请直接回车:  ')
	if raw == '':
		length = random.choice(range(5,51))
		print('已随机长度。')
	else:
		try:
			length = int(raw)	
			assert 5 <= length <= 50
		except:
			print('输入有误，请输入5~50的数字。')
			exit()
	
	if(gender == 'f'):
		name = create_name(femalepieces,length,firstname,lastname)
	elif(gender == 'm'):
		name = create_name(malepieces,length,firstname,lastname)
	
	print('名字为：{}'.format(name))

	