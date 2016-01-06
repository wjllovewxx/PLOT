from flask import Flask, redirect, url_for, render_template
import webbrowser
import threading
import creeper
import para

app = Flask(__name__)

def link_wrap(url):
    return '<input type="image" src="' + url + '">  </input>'


def extend(link_block):
    for link_list in link_block:
        for link in link_list:
            para.LINK_DICT[link.md5()] = link.large

@app.route('/plot/')
def plot():
    link_block, para.NEXT_URL = creeper.creep(para.HOME_URL)
    extend(link_block)
    return render_template('plot.html', link_block=link_block)


@app.route('/home/')
def home():
    link_block, para.NEXT_URL = creeper.creep(para.HOME_URL)
    extend(link_block)
    return render_template('part.html', link_block=link_block)


@app.route('/next/')
def next():
    link_block, para.NEXT_URL = creeper.creep(para.NEXT_URL)
    extend(link_block)
    return render_template('part.html', link_block=link_block)


@app.route('/plot/download/<md5>')
def download(md5):
    #global LINK_DICT, SAVE_PATH
    stat = False
    try:
        opener = creeper.make_my_opener()
        link = para.LINK_DICT[md5]
        suffix = link[len(link)-4:len(link)]
        date = opener.open(link, timeout=1000).read()
        file = open(para.SAVE_PATH + md5 + suffix, 'wb')
        file.write(date)
    finally:
        file.close()
    return stat


if __name__ == '__main__':
    # app.run()
    #global COOKIE

    f = open('cookie')
    line = f.readline()
    if len(line) == 0:
        print("找不到cookie！\n按Enter退出程序")
        input()
        exit()
    else:
        para.COOKIE = line

    thread = threading.Thread(target = app.run)
    thread.start()
    # webbrowser.open_new_tab('http://127.0.0.1:5000/login/')
    webbrowser.open_new_tab('http://127.0.0.1:5000/plot/')