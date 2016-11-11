#coding:utf-8
from django.shortcuts import render_to_response
from django.http import HttpResponse
from app1.models import *
from app1.paixu import px
from django.shortcuts import  render
import os
from django.contrib.auth.decorators import login_required
import time
import sys
from config import config as s
import copy


def wlog(args,args2,username,regip):
    a=os.path.split(os.path.realpath(__file__))[0]
    data = time.strftime("%y%m%d", time.localtime(time.time()))
    udata = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
    username = username
    with open(a+'/'+'log'+'/'+data+ '.log','a+') as w:
	w.write('\nUser:%s IP:%s Update:%s Project:%s UpVersion:%s' %(username,regip,udata,args2,args))

def updt(user,c,pth,b,username,regip):
    linux = ''
    pas='IPfyfXtStu8TZWt0'
    svnuser='svnban'
    if c:
	import threading
	lock = threading.RLock()
	lock.acquire()
        os.popen('ssh -p 22 %s@%s /bin/rm -rf %s' %(user,s.server[b][0],s.server[b][1]))
        linux = os.popen('ssh -p 22 %s@%s %s export %s %s --username %s --password %s --no-auth-cache --force' %(user,s.server[b][0],pth,c,s.server[b][1],svnuser,pas) )
        time.sleep(1)
        os.popen('ssh -p 22 %s@%s /bin/chmod -R 755 %s' %(user,s.server[b][0],s.server[b][1]))
        lock.release()
	wlog(c,b,username,regip)
    else:
        linux = '输入错误'
        wlog(c,b,username,regip)
    return linux

def index(request):
	return render_to_response('index.html')

@login_required
def loop(request):
	ob_dir='svn://127.0.0.1/'
        b=request.REQUEST.get('projet')
	c=str(request.REQUEST.get('version')).strip()
	a=os.path.split(os.path.realpath(__file__))[0] #获取当前目录
	username = request.user.username #获取用户名
	puser='root'
	regip = 'apache'
	pth = '/usr/local/svn/bin/svn'
	up_ob=''
	obj_html=s.server.keys()
	if b in obj_html and c == 'trunk':
	   up_ob = ob_dir+b[1:]+'/trunk/'
	   linux = updt('www',ob_dir+b[1:]+'/trunk/','/usr/bin/svn',b,username,regip)
	elif b in obj_html and c:
	   up_ob = ob_dir+b[1:]+'/branches/'+c
	   linux = updt('www',ob_dir+b[1:]+'/branches/'+c,'/usr/bin/svn',b,username,regip)
	else:
	   linux = '输入错误'
	return render_to_response('loop.html',{'linux':linux,'obj_html':obj_html,'up_ob':up_ob})


