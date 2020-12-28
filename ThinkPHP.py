#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = ddking''

import sys
import requests
from bs4 import BeautifulSoup
from requests.packages.urllib3.exceptions import InsecureRequestWarning
import re
import time

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
reload(sys)
sys.setdefaultencoding('utf-8')
header = dict()
header[ "User-Agent"] = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
#proxy = {'http': 'http://127.0.0.1:8080'}

def poc(url):
    result = ''
    req = requests.get(url,headers=header,verify=False,allow_redirects=False)
    for key in req.headers:                                               #利用响应头判断
        match_key = req.headers[key].lower()
        #print match_key
        if match_key.find('thinkphp') != -1 or match_key.find('think_template') != -1:
            result = ("[ThinkPHP]  "+url)
            break
    if result == '':
        result = error_check(url)
        return result
    else:
        return result


def error_check(url):
        result = ''
        error_url = url+"/index.php/aaass/"
        time.sleep(1)
        req2 = requests.get(error_url,headers=header,verify=False)
        soup = BeautifulSoup(req2.text, 'html.parser')
        if "Think.class.php" in soup.text:
            result = "[ThinkPHP]  " + url
        elif "thinkphp" in soup.text.lower():
            result = "[ThinkPHP]  " + url
        elif soup.h1 != None:
            line = soup.h1.text
            match_key = line.decode('utf-8').strip()
            if re.match(u'\u9875\u9762\u9519\u8bef\uff01\u8bf7\u7a0d\u540e\u518d\u8bd5', match_key):
                result = "[ThinkPHP]  " + url
        return result

def favicon_check():
    pass
