# -*- coding: utf-8 -*-
# @Author  : hakusai
# @Time    : 2022/6/26 18:18

import sys
import re
import datetime
import urllib.request
import time
import random
from pathlib import Path

if __name__ == '__main__':
    max_days = 1
    if len(sys.argv) == 2:
        max_days = int(sys.argv[1])

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36'}

    wallpaper = Path("wallpaper")
    if not wallpaper.exists():
        wallpaper.mkdir()

    for i in range(max_days, 0, -1):
        cur_date = datetime.date.today() - datetime.timedelta(days=1)
        webpage = f"https://bing.wallpaper.pics/us/{cur_date.strftime('%Y%m%d')}.html"
        webpage_url = urllib.request.Request(webpage, headers=headers)
        print(webpage)
        with urllib.request.urlopen(webpage_url, timeout=20) as f:
            data = f.read()
            print(f.read())
        content = data.decode("utf-8")
        for g in re.finditer("src=\'(//[^\']*.jpg)", content):
            pic_url = "http:" + g.group(1)
            print(pic_url)
            pic_name = re.search("([^/.&]*\.jpg)", pic_url).group(1)
            if not (wallpaper / pic_name).exists():
                urllib.request.urlretrieve(pic_url, wallpaper / pic_name)
        time.sleep(random.randint(1, 5))
