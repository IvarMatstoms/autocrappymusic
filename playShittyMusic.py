import requests
import json
import os
import sys
headers = {
        'User-Agent': 'play shitty music by /u/KohaIvar'
        }
go=1
after=""
while go:
    afterop=""
    if after!="":
        afterop="&after=t3_"+after	
    r=requests.get("https://www.reddit.com/r/crappymusic/hot/.json"+afterop,headers=headers)
    music=json.loads(r.text)
    for post in music["data"]["children"]:
            url=post["data"]["url"]
            if ("youtube.com" in url and "v=" in url) or ("youtu.be" in url):
                        os.system("rm /tmp/shitmusic.wav > /dev/null 2> /dev/null ")
                        cmd="youtube-dl --audio-format wav --extract-audio --output '/tmp/shitmusic.%(ext)s' '"+url+"'"
                        #print (url)
                        #print (cmd)
                        #sys.exit(0)
                        print ("downloading...")
                        os.system(cmd + "> /dev/null 2> /dev/null")
                        print ("playing "+post["data"]["title"])
                        print ("press ctrl+c for next song and ctrl+z to exit")
                        os.system("aplay /tmp/shitmusic.wav > /dev/null 2> /dev/null")
                        #c=input()		
                        #if c=="q":
            after=post["data"]["id"]
