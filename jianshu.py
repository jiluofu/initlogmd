#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Required
- requests (必须)
- pillow (可选)
Info
- author : "zhuxu"
- email  : "zhu.xu@qq.com"
- date   : "2016.11.11"
Update

'''
import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re
import time
import os.path
try:
    from PIL import Image
except:
    pass

import json
import string
import configparser
from selenium import webdriver

conf_path = '/Users/zhuxu/Documents/mmjstool/synctoweb/syncart/sync.conf'
chromedriver_path = '/Users/zhuxu/Documents/mmjstool/chromedriver'
note_file_path = '/Users/zhuxu/Documents/mmjstool/initlogmd/output/art'

cf = configparser.RawConfigParser()
cf.read(conf_path)
username = cf.get('jianshu', 'username')
password = cf.get('jianshu', 'password')
cookie = cf.get('jianshu', 'cookie')

agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
headers = {
    'Host': 'www.jianshu.com',
    'Referer': 'https://www.jianshu.com/',
    'User-Agent': agent
}

# 使用登录cookie信息
session = requests.session()




def initial():

    print('init jianshu')
    try:
        if checkLogin() != True:
            cookie = getCookie();
    except Exception as e:
        
        cookie = getCookie();


def checkLogin():

    
    url = 'https://www.jianshu.com'
    headers = {

        'Host': 'www.jianshu.com',
        'Origin': 'https://www.jianshu.com',
        'Referer': 'https://www.jianshu.com',
        'User-Agent': agent,
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': cookie

    }



    # 通过get_url，使得session获得专栏的cookie，里面有X-XSRF-TOKEN
    login_page = session.get(url, headers=headers, allow_redirects=False);
    

    pattern = r'摹喵居士'
    res = re.findall(pattern, login_page.text)
    if len(res) > 0:
        print('jianshu cookie is ok.')
        return True;
    else:
        return False;

def getCookie():

        url = 'https://www.jianshu.com/sign_in'
        driver = webdriver.Chrome(chromedriver_path)
        driver.get(url)
        time.sleep(5)
        # print(username)
        driver.find_element_by_id('session_email_or_mobile_number').send_keys(username)
        driver.find_element_by_id('session_password').send_keys(password)

        input('去手动登录吧\n>  ')
        # 网页源码
        page = driver.page_source
        # print(page)

        pattern = r'(摹喵居士)'
        res = re.findall(pattern, page)
        # print(res)

        cookies = driver.get_cookies()
        cookies_str = ''
        for item in cookies:
            cookies_str += item['name'] + '=' + item['value'] + ';'
        cf.set('jianshu', 'cookie', cookies_str)
        fp = open(conf_path, 'w')
        cf.write(fp)
        fp.close()
        cf.read(conf_path)



        # 关闭浏览器
        driver.close()

        return cookies_str

def createNote(title, content):

    headers = {

        'Accept': 'application/json',
        "Host": "www.jianshu.com",
        "Referer": "https://www.jianshu.com/writer",
        'User-Agent': agent,
        'Origin': 'https://www.jianshu.com',
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': cf.get('jianshu', 'cookie')
        # 'Cookie': 'read_mode=day; default_font=font1; locale=zh-CN; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1531287771,1531288222,1531289360,1531289395; remember_user_token=W1s1MTAwMV0sIiQyYSQxMCRXeDNPa2hvOWIxUXlVWjV6Znlnc0xPIiwiMTUzMTQ0NjI0Ni43MjgxODE0Il0%3D--4ca3584ff9576a2e8248e8c78a5a1613bd1e9958; _m7e_session=0fbad7453cd6f70fbff6dfa8f501e556; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22164407a98a17cc-08e65f1d4f16db-17366952-1296000-164407a98a2590%22%2C%22%24device_id%22%3A%22164407a98a17cc-08e65f1d4f16db-17366952-1296000-164407a98a2590%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1531448874'
    }
    

    data = {

        'at_bottom': True,
        'notebook_id': '100652',
        'title': title,
        'content': content
    }
    print(title)

    post_url = 'https://www.jianshu.com/author/notes'
    login_page = session.post(post_url, data=json.dumps(data), headers=headers, allow_redirects=False)
    print(login_page.text)
    res = json.loads(login_page.text)

    data = {

        'autosave_control': 1,
        'content': content,
        'id': res['id'],
        'title': title
    }

    post_url = 'https://www.jianshu.com/author/notes/' + str(res['id'])
    print(post_url)
    login_page = session.put(post_url, data=json.dumps(data), headers=headers, allow_redirects=False)
    print(login_page)
    print(login_page.text)
    # res = json.loads(login_page.text)

def pubNotes():

    noteArr = os.listdir(note_file_path)
    noteArr.sort()
    
    for i in range(0, len(noteArr)):
        pattern = r'([^\.]*\.)*md$'
        if re.match(pattern, noteArr[i]):
            title = noteArr[i].replace('.md', '').replace('~', '~*')
            file_path = note_file_path + os.path.sep + noteArr[i]
            fp = open(file_path, 'r', encoding='utf-8')
            content = fp.read()
            fp.close()
            createNote(title, content)
            time.sleep(1)
            os.remove(file_path)

def fetch_notes(root_path, notebook_id, cookie):

    headers_notes = {
        'Host': 'www.jianshu.com',
        'Origin': 'https://www.jianshu.com',
        'Referer': 'https://www.jianshu.com/writer',
        'User-Agent': agent,
        'Content-Type': 'application/json;charset=UTF-8',
        'Cookie': 'read_mode=day; locale=zh-CN; default_font=font1; __yadk_uid=XQyGPOzkWKCP8ofJfoNbjuE5ytSOZxw0; Hm_lvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1567301105,1567327851,1567328444,1567338882; remember_user_token=W1s1MTAwMV0sIiQyYSQxMCRXeDNPa2hvOWIxUXlVWjV6Znlnc0xPIiwiMTU2NzM3NjIyNi4yNDQwOTU2Il0%3D--4c9a6463bae217a4a888938856df72caf49b6724; _m7e_session_core=f3a7cccfb2a027e053253d2cf817403a; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2216ce7515f886e6-0551eea721aaca-38637701-2073600-16ce7515f898bd%22%2C%22%24device_id%22%3A%2216ce7515f886e6-0551eea721aaca-38637701-2073600-16ce7515f898bd%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_referrer%22%3A%22%22%2C%22%24latest_referrer_host%22%3A%22%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%7D%2C%22first_id%22%3A%22%22%7D; Hm_lpvt_0c0e9d9b1e7d617b3e6842e85b9fb068=1567376519'

    }
    url = 'https://www.jianshu.com/author/notes/52451432/content'
    res = session.get(url, headers=headers).text
    print(res)
        

initial()
# pubNotes() 
fetch_notes('', '', '')



    


