#!/usr/bin/env python
# coding:utf-8
# day 6.1

'''
有了web框架和orm框架，我们就可以开始装配app了
通常，一个web app在运行时，都需要读取配置文件，比如数据库的用几名、口令等
在不同环境中运行时，web app可以通过读取不同的配置文件来获得正确的配置


这里就是默认的配置文件
'''

configs = {
	'debug': True,
	'db': {
		'host': '127.0.0.1',
		'port': 3306,
		'user': 'root',  # 源码'www-data'
		'password': '079450',   # 源码'www-data'
		'db': 'awesome'
	},
	'session': {
		'secret': 'AwEsOmE'
	}
}