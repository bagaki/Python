#!/usr/bin/env python
# coding:utf-8
# day 5.2

'''
第一步，编写一个用@asyncio.coroutine装饰的函数：
@asyncio.coroutine
def handle_url_xxx(request):
	pass

第二步，传入的参数需要自己从request中获取：
url_param = request.match_info['key']
query_params = parse_qs(requeset.query_string)

最后，需要自己构造Response对象：
text = render('template', data)
return web.Response(text.encode('utf-8'))

这些重复的工作可以由框架完成。
例如，处理带参数的URL/blog/{id}可以这么写：
@get('/blog/{id}')
def get_blog(id):
	pass
等等...
'''

import asyncio, os, inspect, logging, functools
from urllib import parse
from aiohttp import web
from apis import APIError


# @get和@post
# 要把一个函数映射为一个URL处理函数，先定义@get()
# 这样，一个函数通过@get()的装饰就附带了URL信息
# @post和@get定义类似
def get(path):
	'''
	define decorator @get('/path')
	'''

	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			return func(*args, **kw)
		wrapper.__method__ = 'GET'
		wrapper.__route__ = path
		return wrapper
	return decorator


def post(path):
	'''
	define decorator @post('/path')
	'''
	def decorator(func):
		@functools.wraps(func)
		def wrapper(*args, **kw):
			return func(*args, **kw)
		wrapper.__method__ = 'POST'
		wrapper.__route__ = path
		return wrapper
	return decorator


# 运用inspect模块，创建几个函数用以获取URL处理函数与request参数之间的关系
def get_required_kw_args(fn):   # 收集没有默认值的命名关键参数
	args = []
	params = inspect.signature(fn).parameters  # inspect模块是用来分析模块，函数
	for name, param in params.items():
		if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
			args.append(name)
	return tuple(args)


# 获取命名关键字参数
def get_named_kw_args(fn):
	args = []
	params = inspect.signature(fn).parameters
	for name, param in params.items():
		if param.kind == inspect.Parameter.KEYWORD_ONLY:
			args.append(name)
	return tuple(args)


# 判断有没有命名关键字参数
def has_named_kw_args(fn):
	params = inspect.signature(fn).parameters
	for name, param in params.items():
		if param.kind == inspect.Parameter.KEYWORD_ONLY:
			return True


# 判断有没有关键字参数
def has_var_kw_arg(fn):
	params = inspect.signature(fn).parameters
	for name, param in params.items():
		if param.kind == inspect.Parameter.VAR_KEYWORD:
			return True


# 判断是否含有名叫'request'参数，且该参数是否为最后一个参数
def has_request_arg(fn):
	sig = inspect.signature(fn)
	params = sig.parameters
	found = False
	for name, param in params.items():
		if name == 'request':
			found = True
			continue
		if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
			raise ValueError('request parameter must be the last named parameter in function: {}{}'.format(fn.__name__, str(sig)))
	return found


# 定义RequestHandler，正式向request参数获取URL处理函数所需的参数
class RequestHandler(object):

	# 接收app参数
	def __init__(self, app, fn):
		self._app = app
		self._func = fn
		self._has_request_arg = has_request_arg(fn)
		self._has_var_kw_arg = has_var_kw_arg(fn)
		self._has_named_kw_args = has_named_kw_args(fn)
		self._named_kw_args = get_named_kw_args(fn)
		self._required_kw_args = get_required_kw_args(fn)

    # __call__这里要构造协程
	async def __call__(self, request):
		kw = None
		if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
			# 判断客户端发来的方法是否为POST
			if request.method == 'POST':
				# 查询有没提交数据的格式
				if not request.content_type:
					return web.HTTPBadRequest(text = 'Missing Content_type.')
				ct = request.content_type.lower()
				if ct.startswith('application/json'):
					# read request body decode as json
					params = await request.json()
					if not isinstance(params, dict):
						return web.HTTPBadRequest(text = 'JSON body must be object.')
					kw = params
				elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
					# reads POST parameters from request body. 
					# If method is not POST, PUT, PATCH, TRACE or DELETE or content_type is not empty or application/x-www-form-urlencoded or multipart/from-data returns empty multidict
					params = await request.post()
					kw = dict(**params)
				else:
					return web.HTTPBadRequest(text = 'Unsupported Content_type: {}'.format(request.content_type))
			if request.method == 'GET':
				# The query string in the URL
				qs = request.query_string
				if qs:
					kw = dict()
					# parse a query string given as a string argument. 
					# Data are returned as a dictionary.
					# The dictionary keys are the unique query variable names and the values are lists of values for each name.
					for k, v in parse.parse_qs(qs, True).items():
						kw[k] = v[0]
		if kw is None:
			kw = dict(**request.match_info)
		else:
			if not self._has_var_kw_arg and self._named_kw_args:
				# 当函数参数没有关键字参数时，移去request除命名关键字参数所有的参数信息
				# remove all unamed kw:
				copy = dict()
				for name in self._named_kw_args:
					if name in kw:
						copy[name] = kw[name]
				kw = copy
			# check named arg:检查命名关键参数
			for k, v in request.match_info.items():
				if k in kw:
					logging.warning('Duplicate arg name in named arg and kw args: {}'.format(k))
				kw[k] = v
		if self._has_request_arg:
			kw['request'] = request
		# check required kw
		# 假如命名关键字参数（没有附加默认值），request没有提供相应的数值，报错
		if self._required_kw_args:
			for name in self._required_kw_args:
				if not name in kw:
					return web.HTTPBadRequest('Missing argument: {}'.format(name))
		logging.info('call with args: {}'.format(str(kw)))
		try:
			r = await self._func(**kw)
			return r
		except APIError as e:
			return dict(error=e.error, data=e.data, message=e.message)


# 添加静态文件夹的路径
def add_static(app):
	# 输出当前文件夹中'static'的路径
	path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
	# prefix (str) - URL path prefix for handled static files
	app.router.add_static('/static/', path)
	logging.info('add static {} => {}'.format('/static/', path))


# 编写一个add_route函数，用来注册一个URL处理函数
def add_route(app, fn):
	method = getattr(fn, '__method__', None)
	path = getattr(fn, '__route__', None)
	if path is None or method is None:
		raise ValueError('@get or @post not defind in {}.'.format(str(fn)))
	# 判断是否为协程且生成器
	if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
		fn = asyncio.coroutine(fn)
	logging.info('add route {} {} => {}({})'.format(method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
	app.router.add_route(method, path, RequestHandler(app, fn))


# 直接导入文件，批量注册一个URL处理函数
def add_routes(app, module_name):
	n = module_name.rfind('.')
	if n == (-1):
		mod = __import__(module_name, globals(), locals())
	else:
		name = module_name[n+1:]
		# 第一个参数为文件路径参数，不能掺夹函数名，类名
		mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
	for attr in dir(mod):
		if attr.startswith('_'):
			continue
		fn = getattr(mod, attr)
		if callable(fn):
			method = getattr(fn, '__method__', None)
			path = getattr(fn, '__route__', None)
			# 这里要查询path以及method是否存在而不是等待add_route函数查询，因为那里错误就要报错了
			if method and path:
				add_route(app, fn)


# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# # 

# import asyncio, os, inspect, logging, functools

# from urllib import parse

# from aiohttp import web

# from apis import APIError

# def get(path):
#     '''
#     Define decorator @get('/path')
#     '''
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             return func(*args, **kw)
#         wrapper.__method__ = 'GET'
#         wrapper.__route__ = path
#         return wrapper
#     return decorator

# def post(path):
#     '''
#     Define decorator @post('/path')
#     '''
#     def decorator(func):
#         @functools.wraps(func)
#         def wrapper(*args, **kw):
#             return func(*args, **kw)
#         wrapper.__method__ = 'POST'
#         wrapper.__route__ = path
#         return wrapper
#     return decorator

# def get_required_kw_args(fn):
#     args = []
#     params = inspect.signature(fn).parameters
#     for name, param in params.items():
#         if param.kind == inspect.Parameter.KEYWORD_ONLY and param.default == inspect.Parameter.empty:
#             args.append(name)
#     return tuple(args)

# def get_named_kw_args(fn):
#     args = []
#     params = inspect.signature(fn).parameters
#     for name, param in params.items():
#         if param.kind == inspect.Parameter.KEYWORD_ONLY:
#             args.append(name)
#     return tuple(args)

# def has_named_kw_args(fn):
#     params = inspect.signature(fn).parameters
#     for name, param in params.items():
#         if param.kind == inspect.Parameter.KEYWORD_ONLY:
#             return True

# def has_var_kw_arg(fn):
#     params = inspect.signature(fn).parameters
#     for name, param in params.items():
#         if param.kind == inspect.Parameter.VAR_KEYWORD:
#             return True

# def has_request_arg(fn):
#     sig = inspect.signature(fn)
#     params = sig.parameters
#     found = False
#     for name, param in params.items():
#         if name == 'request':
#             found = True
#             continue
#         if found and (param.kind != inspect.Parameter.VAR_POSITIONAL and param.kind != inspect.Parameter.KEYWORD_ONLY and param.kind != inspect.Parameter.VAR_KEYWORD):
#             raise ValueError('request parameter must be the last named parameter in function: %s%s' % (fn.__name__, str(sig)))
#     return found

# class RequestHandler(object):

#     def __init__(self, app, fn):
#         self._app = app
#         self._func = fn
#         self._has_request_arg = has_request_arg(fn)
#         self._has_var_kw_arg = has_var_kw_arg(fn)
#         self._has_named_kw_args = has_named_kw_args(fn)
#         self._named_kw_args = get_named_kw_args(fn)
#         self._required_kw_args = get_required_kw_args(fn)

#     async def __call__(self, request):
#         kw = None
#         if self._has_var_kw_arg or self._has_named_kw_args or self._required_kw_args:
#             if request.method == 'POST':
#                 if not request.content_type:
#                     return web.HTTPBadRequest('Missing Content-Type.')
#                 ct = request.content_type.lower()
#                 if ct.startswith('application/json'):
#                     params = await request.json()
#                     if not isinstance(params, dict):
#                         return web.HTTPBadRequest('JSON body must be object.')
#                     kw = params
#                 elif ct.startswith('application/x-www-form-urlencoded') or ct.startswith('multipart/form-data'):
#                     params = await request.post()
#                     kw = dict(**params)
#                 else:
#                     return web.HTTPBadRequest('Unsupported Content-Type: %s' % request.content_type)
#             if request.method == 'GET':
#                 qs = request.query_string
#                 if qs:
#                     kw = dict()
#                     for k, v in parse.parse_qs(qs, True).items():
#                         kw[k] = v[0]
#         if kw is None:
#             kw = dict(**request.match_info)
#         else:
#             if not self._has_var_kw_arg and self._named_kw_args:
#                 # remove all unamed kw:
#                 copy = dict()
#                 for name in self._named_kw_args:
#                     if name in kw:
#                         copy[name] = kw[name]
#                 kw = copy
#             # check named arg:
#             for k, v in request.match_info.items():
#                 if k in kw:
#                     logging.warning('Duplicate arg name in named arg and kw args: %s' % k)
#                 kw[k] = v
#         if self._has_request_arg:
#             kw['request'] = request
#         # check required kw:
#         if self._required_kw_args:
#             for name in self._required_kw_args:
#                 if not name in kw:
#                     return web.HTTPBadRequest('Missing argument: %s' % name)
#         logging.info('call with args: %s' % str(kw))
#         try:
#             r = await self._func(**kw)
#             return r
#         except APIError as e:
#             return dict(error=e.error, data=e.data, message=e.message)

# def add_static(app):
#     path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'static')
#     app.router.add_static('/static/', path)
#     logging.info('add static %s => %s' % ('/static/', path))

# def add_route(app, fn):
#     method = getattr(fn, '__method__', None)
#     path = getattr(fn, '__route__', None)
#     if path is None or method is None:
#         raise ValueError('@get or @post not defined in %s.' % str(fn))
#     if not asyncio.iscoroutinefunction(fn) and not inspect.isgeneratorfunction(fn):
#         fn = asyncio.coroutine(fn)
#     logging.info('add route %s %s => %s(%s)' % (method, path, fn.__name__, ', '.join(inspect.signature(fn).parameters.keys())))
#     app.router.add_route(method, path, RequestHandler(app, fn))

# def add_routes(app, module_name):
#     n = module_name.rfind('.')
#     if n == (-1):
#         mod = __import__(module_name, globals(), locals())
#     else:
#         name = module_name[n+1:]
#         mod = getattr(__import__(module_name[:n], globals(), locals(), [name]), name)
#     for attr in dir(mod):
#         if attr.startswith('_'):
#             continue
#         fn = getattr(mod, attr)
#         if callable(fn):
#             method = getattr(fn, '__method__', None)
#             path = getattr(fn, '__route__', None)
#             if method and path:
#                 add_route(app, fn)