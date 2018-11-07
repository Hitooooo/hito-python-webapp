#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" url handlers """

import re, time, json, logging, hashlib, base64, asyncio

from www.coroweb import get, post

from www.model.user import User, Comment, Blog, next_id


@get('/')
async def index(request):
    summary = 'This a simple test!'
    blogs = [
        Blog(id='1', name='Test Blog', summary=summary, created_at=time.time() - 120),
        Blog(id='2', name='Something New', summary=summary, created_at=time.time() - 3600),
        Blog(id='3', name='Learn Swift', summary=summary, created_at=time.time() - 7200)
    ]
    return {
        '__template__': 'blogs.html',
        'blogs': blogs
    }


@get('/api/users')
def api_get_users(*, page='1'):
    users = yield from User.findAll(orderBy='created_at desc')
    for u in users:
        u.passwd = '******'
    return dict(users=users)


@get('/register')
def register():
    return {
        '__template__': 'register.html'
    }
