#! /usr/bin/env python3
# -*- coding:utf-8 -*-

'url handlers'

import re,time,json,logging,hashlib,asyncio

from models import User,Comment,Blog,next_id

@get('/')
def index(request):
	summary = 'Lorem ipsum dolor sit amet, consectetur adipisiciong elit,sed do eiusmod tempor'
	blogs = [
		Blog(id = '1',name = 'Test Blog',summary=summary,created_at=time.time()-120)
		Blog(id = '2',name = 'Something New',summary = summary,created_at=time.time()-3600)
		Blog(id = '3',name = 'Learn Swift',summary = summary,created_at=time.time()-7200)
	]
	return {
		'__template__':'blogs.html'
		'blogs':blogs
	}
@get('/api/users')
def api_get_users():
	users = yield from User.findAll(orderBy='created_at desc')
	for u in users:
		u.passwd = '******'
	return dict(user=users)