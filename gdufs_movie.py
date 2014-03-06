# -*- coding: UTF-8 -*-

import urllib
import urllib2
import cookielib
import re

#登录GDUFS 获取cookies
cookie = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookie))
postdata=urllib.urlencode({
	'username':'20121003800',
	'password':'287310',
	'login-form-type':'pwd',
	})

req = urllib2.Request(
	url  = 'http://jw.gdufs.edu.cn/pkmslogin.form',
	data = postdata
	)
opener.open(req)
#跳影片库
opener.open('http://lbxt.gdufs.edu.cn/web/gethead.asp')
scannerUrl='http://lbxt.gdufs.edu.cn/web/VOD/vod_SourceList.asp?groupid=1&FirstTypeID=0&SecondTypeID=0&ThirdTypeID=0&FourthTypeID=0&'
movieReq = urllib2.Request(scannerUrl+'Page=2')
movieReq.add_header('User-Agent','Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E; 360SE)')
tmp = opener.open(movieReq)

pattern = re.compile(r'[^a]*?alt=\"([^\"]*?\".*?jpg)')
nameP = re.compile(r'([^"]*?)".*?src')
downP = re.compile(r'src=\"([^\j]*?)j')
item = pattern.findall(tmp.read())
arr=[]
for ite in item:
    name = nameP.findall(ite)
    down = downP.findall(ite)
    print name[0].decode('utf-8')
    print down[0].decode('utf-8')




