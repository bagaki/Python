#!/usr/bin/env python
# coding:utf-8
# day 6.2

'''
在config_default.py已经配置好。但是如果要部署到服务器时，通常需要修改数据库的host等信息
直接修改config_default.py并不是一个好办法，更好的方法时编写一个config_override.py
用来覆盖某些默认设置
'''

configs = {
	'db': {
		'host': '127.0.0.1'
	}
}