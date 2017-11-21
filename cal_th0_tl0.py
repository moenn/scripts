osc = [float(n) for n in input("晶振频率(单位 Mhz):  ").split()]
time = [int(n) for n in input("定时时间(单位 ms):  ").split()] 
print(osc)
print(time)
set_number = []
for o,t in zip(osc,time):
	set_number.append(pow(2,16) - (o/12)*t*1000)
print(set_number)
print("频率 			定时时间	设定初值 十六进制")
for o,t,n in zip(osc,time,set_number):
	print("{}Mhz {}ms {} {} ".format(o,t,round(n),hex(round(n))))

