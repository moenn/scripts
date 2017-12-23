# '''
# 11/22/2017
# 89c51单片机定时器工作在16位模式下定时初值的计算
# '''


import os
import pickle


def init():
	#第一次使用脚本，创建用于存储历史记录的本地文件
	if not os.path.exists('.\\cal_th0_tl0.pkl'):
		with open('.\\cal_th0_tl0.pkl','wb') as f:
			pickle.dump({'frequency':[12.0],'time':[1.0]},f,-1)

		
def get_data():
	with open('.\\cal_th0_tl0.pkl','rb') as f:
		data = pickle.load(f)
		
		freq_r = input('请输入晶振频率(单位：Mhz,以空格隔开):')
		if freq_r:
			data['frequency'] = [float(n) for n in freq_r.split()]
		
		time_range = [round(pow(2,16)*(12/f)/1000,2) for f in data['frequency']]
		print("\n提示：对应的定时上限为 {} (单位：ms):\n".format(time_range))
		
		time_r = input('请输入定时时间(单位：ms,以空格隔开):')
		if time_r:
			data['time'] =  [float(n) for n in time_r.split()]
	with open('.\\cal_th0_tl0.pkl','wb') as f:
		pickle.dump(data,f,-1)
	
	return data

def cal_setnumber(data):
	setnumber = []
	for f,t in zip(data['frequency'],data['time']):
		setnumber.append(pow(2,16) - (f/12)*t*1000)

	return setnumber

def print_result(data,setnumber):
	print("---------------------------------------------------")
	print("计算结果如下：\n")
	print("频率(Mhz) 定时时间(ms) 设定初值(十进制/十六进制)")
	for f,t,n in zip(data['frequency'],data['time'],setnumber):
		print("{:<10} {:<13} {:<20}".format(f,t,str(round(n)) + '/'+ hex(round(n))))
	
	return None



if __name__ == '__main__':
	init()
	data = get_data()
	setnumber = cal_setnumber(data)
	print_result(data,setnumber)





# class Osc(object):
# 	"""docstring for Osc"""
# 	def __init__(self):
# 		if not os.path.exists('.\\cal_th0_tl0.txt'):
# 				f.write('12.000\n1')

		
# 		with open('.\\cal_th0_tl0.txt','rw') as f:
# 			f = list(f.readlines[0])
# 			timing_history = list(f.readlines[1])

# 			raw_frequency = input('请输入晶振频率(单位：Mhz,以空格隔开)')
# 			if not raw_frequency:
# 				self.frequency = frequency_history
# 			else:
# 				self.frequency = [float(n) for n in raw_frequency.split()]
				
# 			raw_timing = input('请输入定时时间(单位：ms,以空格隔开)')
# 			if not raw_timing:
# 				self.timing = timing_history

# 			else:
# 				self.timing =  [float(n) for n in raw_timing.split()]
# 				f.
# 		self.__frequency = [float(n) for n in raw_frequency.split()] 
		


# 	def get_frequency(self):
# 		return self.__frequency

# 	def set_frequency(self):
# 		return None

# 	def get_timing_time(self):
# 		return self.__timing_time

# 	def set_timing_time(self):
# 		return None

# 	def print_set_number_hex(self):
# 		set_number = []
# 		for f,t in zip(self.__frequency,self.__timing_time):
# 			set_number.append(pow(2,16) - (f/12)*t*1000)
# 		set_number_hex = [hex(round(n)) for n in set_number]
# 		print(set_number_hex)



# osc = Osc()
# osc.set_frequency()
# osc.set_timing_time()
# osc.print_set_number_hex()
