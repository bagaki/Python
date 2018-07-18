#!/usr/bin/env python
# coding:utf-8
# day 6.3

'''
把config_default.py作为开发环境的标准配置，把config_overrisde.py作为生产环境的标准配置
我们就可以既方便在本地开发，又可以随时把应用部署到服务器上

应用程序读取配置文件需要优先从config_override.py读取。
而哦了简化读取配置文件，可以把所有配置读取到统一的config.py
'''

import config_default


class Dict(dict):
	'''
	simple dict but support access as x.y style
	重写属性设置，获取方法
	支持通过属性名 访问键值对的值，属性名将被当作键名
	'''
	def __init__(self, names=(), values=(), **kw):
		super(Dict, self).__init__(**kw)
		# zip函数将参数数据分组返回[(arg1[0], arg2[0], arg3[0]...), (arg1[1], arg2[1], arg3[1])...]
		# 以参数中元素数量最少的集合长度返回列表长度
		for k, v in zip(names, values):
			self[k] = v

	def __getattr__(self, key):
		try:
			return self[key]
		except KeyError:
			raise AttributeError(r"'Dict' object has no attribute '{}'".format(key))

	def __setattr__(self, key, value):
		self[key] = value


def merge(defaults,override):
	r = {}
	for k, v in defaults.items():
		if k in override:
			if isinstance(v, dict):
				r[k] = merge(v, override[k])
			else:
				r[k] = override[k]
		else:
			r[k] = v
	return r


def toDict(d):
	D = Dict()
	for k, v in d.items():
		# 使用三目运算符，如果值是一个dict递归将其转换为Dict再赋值，否则直接赋值
		D[k] = toDict(v) if isinstance(v, dict) else v
	return D


configs = config_default.configs

try:
	import config_override
	configs = merge(configs, config_override.configs)
except ImportError:
	pass


configs = toDict(configs)