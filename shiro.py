#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = ddking


import requests

def poc(url):
    header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0",
              "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
              "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
              "Accept-Encoding": "gzip, deflate",
              "cookie":"rememberMe=1"}
    #proxy = {'http':'http://127.0.0.1:8080'}
    res_get = requests.get(url, headers=header, allow_redirects=False,verify=False)
    result = "[shiro!!!]  "
    try:
        if "rememberMe" in res_get.headers['Set-Cookie']:
            return result+url
        else:res_post = requests.post(url,headers=header,proxies=proxy)
        if "rememberMe" in res_post.headers['Set-Cookie']:
            return result+url
        else:
            return False
    except Exception:
        return False