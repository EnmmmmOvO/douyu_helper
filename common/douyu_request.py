# encoding:utf-8
import requests
from requests.sessions import session
import os


# 重写请求方法,便于直接获取结果
class DYHTTPRequests:

    def __init__(self):
        self.session = session()
        self.header = {
            "Content-Type": "application/x-www-form-urlencoded",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                          "Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.81",
            "referer": "https://www.douyu.com",
            # "Cookie": os.environ["COOKIES"]
            "Cookie": "acf_did=0d945ed357b50e80ee2ee63400021501; smidV2=20200812225411dd9ce861bb73dbcb3ed9a82e200d98250030d6d027feb0d40; dy_did=0d945ed357b50e80ee2ee63400021501; acf_auth=9b2d%2B7HIbcN93owNyhxluSXZDbIUjeijr3SuzqK5OOlMYlmpUlw9e76pvDT%2BSY7ZDihWsF%2B9e7uinRfp352WKqiEqT7roklfKGKZdyYYUnJz56XC9O520%2BVn%2Fiid; dy_auth=1069K%2BpwZTzSB7vN%2BywGtDIgb4Mj8bYAL7%2BGfo0ox%2BaPaLbt98gtRTSj%2BnxGgdYdxk7%2BlFv7Ex%2B2niFGUw4mCKvOOhZQtdutS%2BbGzm5%2Fr2pu1WIzG%2BFj11QD%2BPse; wan_auth37wan=4db49ebaab50%2F44eSE9uMmZhghlGZW6peDEz6tHdB10VfjoxGM%2F0bpsbmqVM5tjQnjtQnyd5Zz37WAQ1BXRJMn%2BYvR6kIB833H%2BwYx65ex%2B58O0u; acf_uid=9096489; acf_username=auto_0ZpUDqZB1y; acf_nickname=%E5%B0%B1%E5%8F%AB%E9%BB%98%E5%A4%9C%E5%90%A7; acf_own_room=1; acf_groupid=1; acf_phonestatus=1; acf_ct=0; acf_ltkid=33163980; acf_biz=1; acf_stk=8c0ac28b474096dc; Hm_lvt_e99aee90ec1b2106afe7ec3b199020a7=1614695816,1614786410,1614869014,1614948448; acf_avatar=//apic.douyucdn.cn/upload/avatar/009/09/64/89_avatar_; PHPSESSID=h7nldknuddcu1s318m8bpj4567; acf_ccn=8e0288a8806b136fb33344ca7acd1049; Hm_lpvt_e99aee90ec1b2106afe7ec3b199020a7=1614949323"
        }

    def __del__(self):
        self.session.close()

    def request(self, method, path, **kwargs):
        url = "https://www.douyu.com" + path
        method.upper()
        return self.session.request(method, url=url, headers=self.header, **kwargs)


dyreq = DYHTTPRequests()

if __name__ == '__main__':
    print(dyreq.request("get", "/lapi/member/api/getInfo").json())