# PLOT - 微博看图助手
本来是一个Python小爬虫，用来爬爬自己的微博首页，看看图啥的。

然后想到可以做成一个魔改的微博客户端，用来去掉微博首页上乱七八糟的东西。

为了做成B/S，用Flask在本地架了一个server。（其实仔细想想都没必要用Python吧，直接js貌似也可以）。

总之不啰嗦了，反正暂时也没几个人看。

###依赖:
 - Flask
 - Beautifulsoup
 - (上面两个都是截止至2016年01月的最新版。包括Python3)

---

###必看:
 - 使用`Python 3`
 - 建议使用**Firefox**或者**Chrome**，否则可能会显示奇奇怪怪的东西(懒得去兼容IE
 - **在文件`cookie`中填入你登陆weibo.cn时抓取的cookie**(懒得做登陆，怕被怀疑盗号
 - `code.py`是程序入口，downloads文件夹下是下载的图片
