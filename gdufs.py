# -*- coding: UTF-8 -*-

import urllib
import urllib2
import cookielib
import re

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
result = opener.open(req)

postdata2 = urllib.urlencode({
	'ddl_ywyl':'有',
        'ddl_kcgs':'',
	'ddl_xqbs':'2',
        'dpkcmcGrid:txtPageSize':'1'
	})
classReq = urllib2.Request(
	url = 'http://jw.gdufs.edu.cn/xf_xsqxxxk.aspx?xh=20121003800&xm=%C0%B5%B3%D0%BA%A3&gnmkdm=N121109',
	data = postdata2
	)
result2 = opener.open(classReq)
ck = result2.read()
pattern = re.compile(r'<a.*?href=.?\'\#\'[^>]*?>([^<]*)')

item = pattern.findall(ck)
for ite in item:
    print ite



