#!/usr/bin/env python
# coding:utf-8
# day 2 + day 5

# __author__ == 'Tomoyababe'

'''
async web application
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment, FileSystemLoader

from config import configs

import orm
from coroweb import add_routes, add_static

from handlers import cookie2user, COOKIE_NAME

# 初始化jinjia2,以便其他函数使用jinja2模板
def init_jinja2(app, **kw):
	logging.info('init jinja2...')
	options = dict(
		autoescape = kw.get('autoescape', True),
		block_start_string = kw.get('block_start_string', '{%'),
		block_end_string = kw.get('block_end_string', '%}'),
		variable_start_string = kw.get('variable_start_string', '{{'),
		variable_end_string = kw.get('variable_end_string', '}}'),
		auto_reload = kw.get('auto_reload', True)
	)
	path = kw.get('path', None)
	if path is None:
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')
	logging.info('set jinja2 template path: {}'.format(path))
	env = Environment(loader=FileSystemLoader(path), **options)
	filters = kw.get('filters', None)
	if filters is not None:
		for name, f in filters.items():
			env.filters[name] = f
	app['__templating__'] = env


async def logger_factory(app, handler):
	async def logger(request):
		logging.info('Request: {} {}'.format(request.method, request.path))
		# await asyncio.sleep(0.3)
		return (await handler(request))
	return logger


async def auth_factorty(app, handler):
	async def auth(request):
		logging.info('check user: {} {}'.format(request.method, request.path))
		request.__user__= None
		cookie_str = request.cookies.get(COOKIE_NAME)
		if cookie_str:
			user = await cookie2user(cookie_str)
			if user:
				logging.info('set current user: {}'.format(user.email))
				request.__user__ = user
		if request.path.startswith('/manager/') and (request.__user__ is None or not request.__user__.admin):
			return web.HTTPFound('/signin')
		return (await handler(request))
	return auth


async def data_factory(app, handler):
	async def parse_data(request):
		if request.method == 'POST':
			if request.content_type.startswith('application/json'):
				request.__data__ = await request.json()
				logging.info('request json: {}'.format(str(request.__data__)))
			elif request.content_type.startswith('application/x-www-form-urlencoded'):
				request.__data__ = await request.post()
				logging.info('request form: {}'.format(str(request.__data__)))
		return (await handler(request))
	return parse_data


async def response_factory(app, handler):
	async def response(request):
		logging.info('Response handler...')
		r = await handler(request)
		if isinstance(r, web.StreamResponse):
			return r
		if isinstance(r, bytes):
			resp = web.Response(body=r)
			resp.content_type = 'application/octet-stream'
			return resp
		if isinstance(r, str):
			if r.startswith('redirect:'):
				return web.HTTPFound(r[9:])
			resp = web.Response(body=r.encode('utf-8'))
			resp.content_type = 'text/html;charset=utf-8'
			return resp
		if isinstance(r, dict):
			template = r.get('__template__')
			if template is None:
				resp = web.Response(body=json.dumps(r, ensure_ascii=False, default=lambda o: o.__dict__).encode('utf-8'))
				resp.content_type = 'application/json;charset=utf-8'
				return resp
			else:
				r['__user__'] = request.__user__
				resp = web.Response(body=app['__templating__'].get_template(template).render(**r).encode('utf-8'))
				resp.content_type = 'text/html;charset=utf-8'
				return resp
		if isinstance(r, int) and t >= 100 and t < 600:
			return web.Response(t)
		if isinstance(r, tuple) and len(r) == 2:
			t, m = r
			if isinstance(t, int) and t >= 100 and t < 600:
				return web.Response(t, str(m))
		# default:
		resp = web.Response(body=str(r).encode('utf-8'))
		resp.content_type = 'text/plain;charset=utf-8'
		return resp
	return response


def datetime_filter(t):
	delta = int(time.time() - t)
	if delta < 60:
		return 'before 1 min'
	if delta < 3600:
		return 'before {} min'.format(delta // 60)
	if delta < 86400:
		return 'before {} hours'.format(delta // 3600)
	if delta < 604800:
		return 'before {} days'.format(delta //86400)
	dt = datetime.fromtimestamp(t)
	return '{} year {} month {} day'.format(dt.year, dt.month, dt.day)



# def index(request):
# 	return web.Response(body=b'<h1>Awesome</h1>', headers = {'content-type': 'text/html'})


# day 2 建立一个在9000端口监听HTTP请求，并响应
async def init(loop):
	await orm.create_pool(loop=loop, **configs.db, charset='utf8')
	app = web.Application(loop=loop, middlewares=[
		logger_factory, auth_factorty, response_factory
	])
	init_jinja2(app, filters=dict(datetime=datetime_filter))
	add_routes(app, 'handlers')
	add_static(app)
	srv = await loop.create_server(app.make_handler(), '127.0.0.1', 9000)
	logging.info('server started at http://127.0.0.1:9000...')
	return srv


loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()

