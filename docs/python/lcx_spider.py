from re import findall
from time import sleep
import requests


end, start = 202227+1, 201980
num = end-start
with open('lcx.html', 'w', encoding='utf-8') as f:
    last_novel = ''
    for i in range(num):
        r = requests.get(
            'http://mliucixin.zuopinj.com/5561/%d.html' % (start+i))
        text = r.text.replace('\r\n', '')
        novel, chapter = findall(
            pattern='<meta name="keywords" content="(.*?)" />', string=text)[0].split(',')
        p = findall(pattern='<p>(.*?)</p>', string=text)[0]
        if novel != last_novel:
            f.write('<h1>%s</h1>\n' % novel)
            last_novel = novel
        f.write('<h2>%s</h2>\n' % chapter)
        print('writing', start+i, novel, chapter)
        f.write(p)
        f.write('\n')
        sleep(0.2)
