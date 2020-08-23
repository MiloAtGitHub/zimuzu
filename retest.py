#-*- codeing = utf-8 -*-
#@Time : 2020-08-21 13:05
#@File : retest.py

import re
findlink = re.compile(r'/level-icon/(.)-big-1.png')
m = re.findall(findlink, "/level-icon/a-big-.png")
print(type(m))
print(m)