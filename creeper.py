import urllib
import hashlib
import http.cookiejar
import cave
import para
from bs4 import BeautifulSoup


class SinaImg:
    __type = ''
    __url = ''
    square = __url.replace(__type, 'square')
    bmiddle = __url.replace(__type, 'bmiddle')
    large = __url.replace(__type, 'large')

    def __init__(self,url):
        if url.find('thumb180') != -1:
            self.__type = 'thumb180'
        elif url.find('wap180') != -1:
            self.__type = 'wap180'
        self.__url = url
        self.square = self.__url.replace(self.__type, 'square')
        self.bmiddle = self.__url.replace(self.__type, 'bmiddle')
        self.large = self.__url.replace(self.__type, 'large')

    def __str__(self):
        return self.__url

    def md5(self):
        return hashlib.md5(self.large.encode()).hexdigest()


def make_my_opener(head={
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, image/jxr, */*',
    'Accept-Language': 'zh-CN',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.11082',   

}):
    head['Cookie'] = para.COOKIE
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def grab_multi_pics(url, save=False):
    opener = make_my_opener()
    data = opener.open(url, timeout = 1000).read()
    soup = BeautifulSoup(data,"html.parser")
    #md5 = hashlib.new("md5")

    link_list = []
    src_list = soup.find_all('img')
    for src in src_list:
        link = SinaImg(src['src'])
        if save:
            src_data = opener.open(link, timeout = 1000).read()
            #md5.update(src_data)
            #md5_str = md5.hexdigest()
            #f = open("E:\\" + md5_str + ".jpg", 'wb')
            #f.write(src_data)
            #f.close()
        else:
            link_list.append(link)
            print(link)

        # time.sleep(random.uniform(0,1))  # 睡眠随机时间
    return link_list


def creep(url):
    opener = make_my_opener()
    data = opener.open(url, timeout = 1000).read()

    soup = BeautifulSoup(data,"html.parser")

    div_list = [] 
    for span in soup.find_all(class_="ctt"):
        div_list.append(span.parent.parent)  # 将满足条件的微博的<div>存放起来

    link_block = []
    for div in div_list:
        skip = False
        a_list = div.find_all('a')  # <div>下的所有<a>
        for a in a_list:
            if a.get_text().find("组图共") != -1:  # 检查<a>
                link_block.append(grab_multi_pics(a['href']))
                skip = True
                break
        if not skip:
            for img in div.find_all(attrs={"alt": "图片"}):
                link_block.append([SinaImg(img['src'])])
                break

    for d in soup.find_all(id="pagelist"):
        if d.a.get_text().find("下页") != -1:
            next_url = para.HOME_URL + d.a['href']

    return link_block, next_url
    # print("end")
