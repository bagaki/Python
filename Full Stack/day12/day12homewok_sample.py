column_dic = {'id': 0, 'name': 1, 'age': 2, 'phone': 3, 'job': 4}

def filter_handler(operate, con):  # '>', 'age>22'
	'''
	进行筛选工作
	:param operate:用户要进行的操作是 > < = like
	:param con:用户输入的where条件
	:return:被选中的所有行组成的列表，其中每一行都是一个列表
	'''
	selected_lst = []  # 被选中的列表
	col, val = con.split(operate)  
	col = col.strip()  # age
	val = val.strip()  # 22
	judge = 'int(line_lst[column_dic[col]]) %s int(val)'%operate if operate == '<' or operate == '>' else 'line_lst[column_dic[col]] %s val'%operate
	f = open('users', encoding = 'utf-8')
	for line in f:
		line_lst = line.strip().split(',')
		if eval(judge):
			selected_lst.append(line_lst)
	f.close()
	return selected_lst


def get_selected_line(con):  # con = 'age>22'
	'''
	获取所有要查找的行，并将每一行作为一个列表项存储字selected_lst中
	：retrun：存储了符合条件的行的列表
	'''
	if '>' in con:
		selected_lst = filter_handler('>', con)
	elif '<' in con:
		selected_lst = filter_handler('<', con)
	elif '=' in con:
		selected_lst = filter_handler('==', con.replace('=', '=='))
	elif 'like' in con:
		selected_lst = filter_handler('in', con)
	return selected_lst


def get_show_lst(col_condition):   # 'select name, age'
	'''
	获取要展示的列名
	:param:col_condition：用户输入的select条件
	:return：列名组成的字典
	'''
	col_info_lst = col_condition.strip().split('select')
	col_info_lst = [col_info_item for col_info_item in col_info_lst if col_info_item.strip()]
	if col_info_lst:   # ['name', 'age']
		col_info = col_info_lst[0].strip()
		if '*' == col_info:
			return column_dic.keys()
		elif col_info:
			ret = col_info.split(',')
			return [item.strip() for item in ret]
		else:
			print(col_info)


def show(selected_lst, show_lst):
	'''
	展示符合条件的内容
	:param selected_lst:符合条件的行的列表
	:param show_lst:所有要展示的字段
	:return：None
	'''
	for select_item in selected_lst:
		for col in show_lst:
			print(select_item[column_dic[col]], end=' ')
		print()

if __name__ == '__main__':
	condition = input('>>> ')
	# 解析用户的指令
	ret = condition.split('where')  # ['select name, age', 'age>22']
	con = ret[1].strip()
	# 根据select条件解析用户需要展示的内容
	show_lst = get_show_lst(ret[0])  # 'select name, age'
	# 根据where条件解析筛选用户向查找的内容
	selected_lst = get_selected_line(con)  # selected_lst中存储了所有符合条件的内容
	# 将符合条件的内容按照用户的需要展示出来
	show(selected_lst, show_lst)