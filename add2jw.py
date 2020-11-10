import geoip2.database
import time


reader = geoip2.database.Reader(r"GeoLite2-City.mmdb")
#reader = geoip2.database.Reader(r"GeoIPCityv6.dat")

def ip_print_AddrInfo(ip):
	# 载入指定IP相关数据
	response = reader.city(ip)
	# 读取国家代码
	Country_IsoCode = response.country.iso_code
	# 读取国家名称
	Country_Name = response.country.name
	# 读取国家名称(中文显示)
	Country_NameCN = response.country.names['zh-CN']
	# Country_NameCN = response.country.names['NA']
	# 读取州(国外)/省(国内)名称
	Country_SpecificName = response.subdivisions.most_specific.name
	# 读取州(国外)/省(国内)代码
	Country_SpecificIsoCode = response.subdivisions.most_specific.iso_code
	# 读取城市名称
	City_Name = response.city.name
	# 读取邮政编码
	City_PostalCode = response.postal.code
	# 获取纬度
	Location_Latitude = response.location.latitude
	# 获取经度
	Location_Longitude = response.location.longitude
	'''
	# 打印
	if ip != None:
		print('[*] Target: ' + ip + ' GeoLite2-Located ')
	if Country_IsoCode != None:
		print('  [+] Country_IsoCode        : ' + Country_IsoCode)
	if Country_Name != None:
		print('  [+] Country_Name           : ' + Country_Name)
	if Country_NameCN != None:
		print('  [+] Country_NameCN         : ' + Country_NameCN)
	if Country_SpecificName != None:
		print('  [+] Country_SpecificName   : ' + Country_SpecificName)
	if Country_SpecificIsoCode != None:
		print('  [+] Country_SpecificIsoCode: ' + Country_SpecificIsoCode)
	if City_Name != None:
		print('  [+] City_Name              : ' + City_Name)
	if City_PostalCode != None:
		print('  [+] City_PostalCode        : ' + City_PostalCode)
	if Location_Latitude != None:
		print('  [+] Location_Latitude      : ' + str(Location_Latitude))
	if Location_Longitude != None:
		print('  [+] Location_Longitude     : ' + str(Location_Longitude))
	'''
	return float(Location_Latitude),float(Location_Longitude),Country_Name



if __name__ == '__main__':
	# print(ip_print_AddrInfo("2001:0:1005:1355:57ae:ce9a:3cb0:9b96"))
	
	start = time.clock()
	
	f = open("head_100w.txt", "r")
	out = open("address-location.txt", "w")
	count = 0
	
	for address in f:
		#去掉每行头尾空白
		address = address.strip()
		try:
			location = ip_print_AddrInfo(address)
			location2file = address + "," + str(location[0]) + "," + str(location[1]) + "," + location[2] + "\n"
			out.write(location2file)
		except:
			count = count + 1
	
	
	print("error: " + str(count))
	f.close()
	out.close()
	
	end = time.clock()
	print('Running time: %s Seconds'%(end-start))