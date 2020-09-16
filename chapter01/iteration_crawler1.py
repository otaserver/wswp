# -*- coding: utf-8 -*-


import itertools
from common import download


def iteration():
    # 使用了itertools来生成序列。
    for page in itertools.count(1):
        # 使用了format函数。
        url = 'http://example.webscraping.com/view/-{}'.format(page)
        html = download(url)
        if html is None:
            # received an error trying to download this webpage
            # so assume have reached the last country ID and can stop downloading
            break
        else:
            # success - can scrape the result
            # ...
            pass


if __name__ == '__main__':
    iteration()
