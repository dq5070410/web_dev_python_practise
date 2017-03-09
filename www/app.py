#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = 'ranger'

'''
asyn web application
'''

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web
from jinja2 import Environment,FileSystemLoader

from config import configs

import orm
from coroweb import add_routes,add_static

def init_jinja2(app,**kw):
	logging.info('init jinja2...')
	options = dict(
			autoescape = kw.get('autoescape',True),
			block_start_string = kw.get('block_start_string','{%'),
			block_end_string = kw.get('block_end_string','%}'),
			variable_start_string = kw.get('variable_start_string','{{'),
			variable_end_string = kw.get('variable_end_string','}}'),
			auto_load = kw.get('auto_load',True)
		)
	path = kw.get('path',None)
	if path is None:
		path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'templates')
	logging.info('set jinja2 template path %s' % path)
	env = Environment(loader = FileSystemLoader(path),**options)
	filters = kw.get('filters',None)
	if filters is not None:
		for name,f in filter.items():
			env.filters[name] = f
	app['__templating__'] = env 

def index(request):
    return web.Response(body=b'<h1>Awesome</h1>',content_type='text/html')

@asyncio.coroutine
def init(loop):
    app = web.Application(loop=loop)
    app.router.add_route('GET', '/', index)
    srv = yield from loop.create_server(app.make_handler(), '192.168.3.119', 9000)
    logging.info('server started at http://192.168.3.119:9000...')
    return srv

loop = asyncio.get_event_loop()
loop.run_until_complete(init(loop))
loop.run_forever()