'''
11/22/2017
89c51单片机定时器工作在16位模式下定时初值的计算
'''

import os

# if first time, create a blank file 
if not os.path.exists('.\\cal_th0_tl0.txt'):
	with open('.\\cal_th0_tl0.txt','w') as f:
		f.write('')

osc_history = []

with open('.\\cal_th0_tl0.txt','r') as f:
	raw_list = f.readlines()
	if not raw_list:
		osc_history.append(12.0000)
	else:
		for n in raw_list:
			osc_history.append(float(n))



raw_string = input("晶振频率(单位 Mhz):  ")
if not raw_string:
	osc = list(osc_history)
	print('你未输入任何数值，将使用上次的晶振数据 {}！\n'.format(osc))
else:
	osc = [float(n) for n in raw_string.split()]
	with open('.\\cal_th0_tl0.txt','w') as f:
		osc_history = [str(n) for n in raw_string.split()]
		f.write(''.join(osc_history))

time_range = []
for o in osc:
	time_range.append(pow(2,16)*(12/o)/1000)
print("注意，对应的定时上限为(单位：ms): {}\n".format(time_range))

time = [float(n) for n in input("定时时间(单位 ms):  ").split()] 
print("---------------------------------------------------")

print("\n晶振频率列表为(单位：Mhz)：{}".format(osc))
print("定时时间列表为(单位：ms):{}\n".format(time))
print("计算结果如下：\n")
set_number = []
for o,t in zip(osc,time):
	set_number.append(pow(2,16) - (o/12)*t*1000)

print("频率(Mhz) 定时时间(ms) 设定初值(十进制) 十六进制")
for o,t,n in zip(osc,time,set_number):
	print("{:<10} {:<13} {:<15} {:<10} ".format(o,t,round(n),hex(round(n))))
