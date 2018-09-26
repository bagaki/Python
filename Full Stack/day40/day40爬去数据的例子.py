import requests
from urllib.request import urlopen
from multiprocessing import Pool


def get(url):
    ret = requests.get(url)
    if ret.status_code == 200:
        return url, ret.content.decode('utf-8')


def get_urllib(url):
    ret = urlopen(url)
    return ret.read().decode('utf-8')


def call_back(args):
    url, content = args
    print(url, len(content))


if __name__ == '__main__':
    url_lst = [
        'http://www.cnblogs.com/',
        'http://www.google.com',
        'http://www.sohu.com',
        'https://www.sogou.com',
    ]
    p = Pool(5)
    for url in url_lst:
        p.apply_async(get, args=(url, ), callback=call_back)
    p.close()
    p.join()
