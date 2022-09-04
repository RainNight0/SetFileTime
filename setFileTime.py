import os
import re
import time

#执行目录，程序将会扫描该目录下的所有对应格式文件
#可使用绝对路径或相对路径
dir_path = './files'
#file_suffix = '.txt'
img_selection_dict = {
	'1' : '.png',
	'2' : '.jpg',
	'3' : '.jpeg',
	'4' : '.txt'
}
date_format_selection_dict = {
	'1' : 'yyyyMMdd-HHmmss',
	'2' : 'yyyy-MM-dd-HH-mm-ss',
	'3' : 'yyyyMMdd_HHmmss',
	'4' : 'yyyy_MM_dd_HH_mm_ss'
}
date_format_regular_dict = {
	'1' : r'(\d{4})(\d{2})(\d{2})-(\d{2})(\d{2})(\d{2})',
	'2' : r'(\d{4})-(\d{2})-(\d{2})-(\d{2})-(\d{2})-(\d{2})',
	'3' : r'(\d{4})(\d{2})(\d{2})_(\d{2})(\d{2})(\d{2})',
	'4' : r'(\d{4})_(\d{2})_(\d{2})_(\d{2})_(\d{2})_(\d{2})'
}

def set_file_time(file,update_time,access_time):
	file = os.path.abspath(file)
	#修改时间
	new_updatetime = time.mktime(time.strptime(update_time, '%Y-%m-%d %H:%M:%S'))
	#访问时间
	new_access_time = time.mktime(time.strptime(access_time, '%Y-%m-%d %H:%M:%S'))
	os.utime(file, (new_updatetime, new_access_time))

#主进程
def main(regular, file_suffix):
	list = os.walk(dir_path)
	for root,dir_list,file_list in list:
		for file_name in file_list:
			file_path = os.path.join(root,file_name)
			#这里设置扫描的文件格式(-4指文件名倒数四位数)
			if file_name[-4:] == file_suffix or file_name[-5:] == file_suffix:
				#print(file_name)
				#取文件名中的时间
				ret = re.match(regular, file_name)
				y, m1, d, h, m2, s = ret.groups()
				file_date = y+'-'+m1+'-'+d+' '+h+':'+m2+':'+s
				print(file_date)
				set_file_time(file_path,file_date,file_date)


def format_selection_list(sd):
	tmp = []
	for k, v in sd.items():
		tmp.append(f'({k}) {v}')
	return '\n'.join(tmp)

#设置参数
def file_format_selection():
	print('请选择文件格式：')
	print(format_selection_list(img_selection_dict))
	while not (img_format := img_selection_dict.get(input())):
		print('非法参数，请重新输入：', end = '')
	print('请选择日期格式：')
	print(format_selection_list(date_format_selection_dict))
	input_date_format = input()
	while not (date_format := date_format_selection_dict.get(input_date_format)):
		print('非法参数，请重新输入：', end = '')
	print(f'你选择的文件格式{img_format}\n'
		f'你选择的日期格式{date_format}')
	regular_format = date_format_regular_dict.get(input_date_format)
	main(regular_format, img_format)


if __name__ == '__main__':
	file_format_selection()


