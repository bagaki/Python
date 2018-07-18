# #!/usr/bin/env python 
# # coding:utf-8
# day 4

import orm
from models import User, Blog, Comment
import asyncio

async def test(loop):
	await orm.create_pool(loop=loop, host='127.0.0.1', port=3306, user='root', password='079450', db='awesome', charset='utf8')
	

	# u = User(name=kw.get('name'), email=kw.get('email'), passwd=kw.get('passwd'), image=kw.get('image'))

	u = User(name='Test', email='278933745@qq.com', passwd='linqi07945', image='about:blank')

	await u.save()
	# await orm.destory_pool()

# data=dict(name='mush2room', email='mush2room@hotmail.com', passwd='138760934622925', image='about:blank')
loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()
if loop.is_closed():
	sys.exit(0)


# import orm
# from Model import User,Blog,Comment
# import asyncio
# loop = asyncio.get_event_loop()
# async def test():
#     #创建连接池,里面的host,port,user,password需要替换为自己数据库的信息
#     await orm.create_pool(loop=loop,host='127.0.0.1', port=3306,user='root', password='079450',db='awesome', charset='utf8')
#     #没有设置默认值的一个都不能少
#     u = User(name='Test', email='idx_email', passwd='linqi07945', image='about:blank', id='PRIMARY')
#     await u.save()

# #把协程丢到事件循环中执行
# loop.run_until_complete(test())