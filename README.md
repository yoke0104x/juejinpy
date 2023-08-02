# juejinpy

## 介绍
此项目是用于掘金自动化签到的，使用python3编写，使用前请先fork本项目，然后再进行下面的操作。

## 使用方法
1. fork本项目
2. 添加环境变量，变量名分别为:
    - JUEJIN_COOKIE: 用于存放掘金的cookie
    - JUEJIN_SENDKEY: 用于向[`server`](https://sct.ftqq.com/sendkey)酱的公众号推送新信息的key
    - JUEJIN_DATA: 用于存放掘金的`aid`信息以及`uuid` 格式为 {aid:xxxx,uuid:xxxx,spider:0}
3. 进入`Actions`，点击`I understand my workflows, go ahead and enable them`



## 说明
如何添加环境变量？
点击`Settings`->`Secrets`->`New repository secret`  


![添加图片](https://img.yoke0104.com/thumbnails/9cebbde0f9aab443854f9b83bc8e28e9.png)