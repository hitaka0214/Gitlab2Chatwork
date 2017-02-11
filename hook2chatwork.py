#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import requests
import pprint

def post_chatwork(msg):
    APIKEY = 'apikey'
    ENDPOINT = 'https://api.chatwork.com/v1'
    ROOMID = 'roomid'
 
    post_message_url = '{}/rooms/{}/messages'.format(ENDPOINT, ROOMID)
 
    headers = {'X-ChatWorkToken': APIKEY}
    params = {'body': msg}
 
    resp = requests.post(post_message_url,
                         headers=headers,
                         params=params)
 
    pprint.pprint(resp.content)

def formatMsg(argvs):
    kind = retObjectKind(argvs[1])
    url = argvs[2]
    state = argvs[3]
    user = argvs[4]
    prj = argvs[5]
    rep_name = argvs[6]
    path_with_namespae = argvs[7]
    commits_message = argvs[8]
    title = argvs[9] if '' != argvs[9] else argvs[10]

    msg  = '[info][title]{} {} {}[/title]'.format(state, kind, prj)
    msg += '{} {} {}'.format(user, title, url)
    msg += '[/info]'
    print(msg)
    
    return msg

def retObjectKind(msg):
    if 'push' == msg:
        return 'pushed'
    elif 'note' == msg:
        return 'created comment'
    elif 'issue' == msg:
        return 'issue'
    else:
        return ''

def main():
    # receive params
    argvs = sys.argv
    print(argvs)

    # create msg
    msg = formatMsg(argvs)
            
    # notificate to chatwork
    post_chatwork(msg)

if __name__ == '__main__':
    main()
